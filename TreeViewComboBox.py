import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from sqlite3 import dbapi2


class Aplicacion (Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo Treeview ComboBox")

        caixaV = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing = 4)

        modelo = Gtk.ListStore(str,str,str)

        try:
            bbdd = dbapi2.connect("bbdd.dat")
        except dbapi2.StandardError as e:
            print(e)
        else:
            print("Base de datos aberta")

        try:
            cursor = bbdd.cursor()
        except dbapi2.Error as e:
            print(e)
        else:
            print("Cursor preparado")

        try:
            consulta = "SELECT * FROM usuarios"
            cursor.execute(consulta)
            for rexistro in cursor.fetchall():
                modelo.append(rexistro)

        except dbapi2.DatabaseError as e:
            print("Erro facendo a cosulta: "+ str(e))
        else:
            print("Consulta executada")
        finally:
            cursor.close()
            bbdd.close()


        self.dniFiltro = None
        self.modeloFiltrado = modelo.filter_new()
        self.modeloFiltrado.set_visible_func(self.dni_filtro_func)

        self.tvwUsuarios = Gtk.TreeView()
        self.tvwUsuarios.set_model(self.modeloFiltrado)


        crtDni = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("DNI",crtDni, text=0)
        self.tvwUsuarios.append_column(columna)

        crtNome = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Nome", crtNome, text=1)
        self.tvwUsuarios.append_column(columna)

        crtDireccion = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("crtDireccion", crtDireccion, text=2)
        self.tvwUsuarios.append_column(columna)


        cmbDni = Gtk.ComboBox.new_with_model(modelo)
        celda = Gtk.CellRendererText()
        cmbDni.pack_start(celda, True)
        cmbDni.add_attribute(celda, "text", 0)
        cmbDni.connect("changed", self.on_cmbDni_changed)

        caixaV.pack_start(cmbDni, False, False, 2)


        caixaV.pack_start(self.tvwUsuarios,True, True, 1)
        self.add(caixaV)

        self.connect ("destroy", Gtk.main_quit)
        self.show_all()

    def on_cmbDni_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            self.dniFiltro = modelo[fila][0]
            self.modeloFiltrado.refilter()



    def dni_filtro_func(self, modelo, fila, data):
        if (self.dniFiltro is None or self.dniFiltro == "None"):
            return True
        else:
            return modelo[fila][0] == self.dniFiltro

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()