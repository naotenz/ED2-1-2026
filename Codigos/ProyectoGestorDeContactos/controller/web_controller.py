import os

from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for

from model.contacto_service import ContactoNoEncontradoError, ContactoService, NombreDuplicadoError


def create_app() -> Flask:
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "view", "templates"))
    app = Flask(__name__, template_folder=template_dir)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")

    service = ContactoService()
    service.cargar_demostracion_si_vacio(
        [
            ("Carlos", "70011001", "carlos@mail.com"),
            ("Ana", "70022002", "ana@mail.com"),
            ("Luis", "70033003", "luis@mail.com"),
            ("Bruno", "70044004", "bruno@mail.com"),
            ("Diana", "70055005", "diana@mail.com"),
            ("Mario", "70066006", "mario@mail.com"),
        ]
    )

    bp = Blueprint("contactos", __name__)

    @bp.get("/")
    def index():
        q = (request.args.get("q") or "").strip()
        contactos = service.buscar(q)
        return render_template("index.html", contactos=contactos, q=q)

    @bp.get("/arbol")
    def arbol():
        arbol_visual = service.visualizar_arbol()
        total = service.total_contactos()
        return render_template("arbol.html", arbol_visual=arbol_visual, total=total)

    @bp.get("/contactos/nuevo")
    def nuevo_get():
        return render_template(
            "form.html",
            modo="nuevo",
            contacto={"nombre": "", "telefono": "", "correo": ""},
            action_url=url_for("contactos.nuevo_post"),
        )

    @bp.post("/contactos/nuevo")
    def nuevo_post():
        nombre = (request.form.get("nombre") or "").strip()
        telefono = (request.form.get("telefono") or "").strip()
        correo = (request.form.get("correo") or "").strip()

        if not nombre:
            flash("El nombre no puede estar vacío.", "error")
            return render_template(
                "form.html",
                modo="nuevo",
                contacto={"nombre": nombre, "telefono": telefono, "correo": correo},
                action_url=url_for("contactos.nuevo_post"),
            )

        try:
            contacto = service.crear(nombre, telefono, correo)
        except (NombreDuplicadoError, ValueError) as e:
            flash(str(e), "error")
            return render_template(
                "form.html",
                modo="nuevo",
                contacto={"nombre": nombre, "telefono": telefono, "correo": correo},
                action_url=url_for("contactos.nuevo_post"),
            )

        flash("Contacto creado correctamente.", "success")
        return redirect(url_for("contactos.editar_get", contacto_id=contacto.id))

    @bp.get("/contactos/<int:contacto_id>/editar")
    def editar_get(contacto_id: int):
        c = service.obtener_por_id(contacto_id)
        if c is None:
            flash("Contacto no encontrado.", "error")
            return redirect(url_for("contactos.index"))
        return render_template(
            "form.html",
            modo="editar",
            contacto={"id": c.id, "nombre": c.nombre, "telefono": c.telefono, "correo": c.correo},
            action_url=url_for("contactos.editar_post", contacto_id=contacto_id),
        )

    @bp.post("/contactos/<int:contacto_id>/editar")
    def editar_post(contacto_id: int):
        telefono = (request.form.get("telefono") or "").strip()
        correo = (request.form.get("correo") or "").strip()

        try:
            c = service.actualizar(contacto_id, telefono, correo)
        except ContactoNoEncontradoError as e:
            flash(str(e), "error")
            return redirect(url_for("contactos.index"))

        flash("Contacto actualizado correctamente.", "success")
        return render_template(
            "form.html",
            modo="editar",
            contacto={"id": c.id, "nombre": c.nombre, "telefono": c.telefono, "correo": c.correo},
            action_url=url_for("contactos.editar_post", contacto_id=contacto_id),
        )

    @bp.get("/contactos/<int:contacto_id>/eliminar")
    def eliminar_get(contacto_id: int):
        c = service.obtener_por_id(contacto_id)
        if c is None:
            flash("Contacto no encontrado.", "error")
            return redirect(url_for("contactos.index"))
        return render_template("confirm_delete.html", contacto=c)

    @bp.post("/contactos/<int:contacto_id>/eliminar")
    def eliminar_post(contacto_id: int):
        try:
            service.eliminar(contacto_id)
            flash("Contacto eliminado correctamente.", "success")
        except ContactoNoEncontradoError as e:
            flash(str(e), "error")
        return redirect(url_for("contactos.index"))

    app.register_blueprint(bp)
    return app
