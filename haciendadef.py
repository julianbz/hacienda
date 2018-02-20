# -*- coding:utf8 -*-
#!/usr/bin/env python
from wx import *
import wx.dataview as dv
import csv, operator
import wx.dataview as dv

class MiApp(App):
    def OnInit(self):
        self.ListaAnimales=[]

#ventana principal
        self.f0=f0=Frame(None, -1, "Control de Hacienda", size = (900,700))
        f0.SetBackgroundColour((255,255,255))
        f0.Maximize(True)
        image_file = 'img/fondo.jpg'
        bmp1= wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.vent10 = wx.StaticBitmap(f0, -1, bmp1,pos=(0,0),size=(1366,768))
        self.vent10.Show()


#botones
        self.boton1=Button(self.vent10,-1,label="",pos=(226,200),size=(250,45))
        self.boton1.SetBitmap(BitmapFromImage(Image("img/cargar_w.jpg")))
        self.boton1.Show()
        self.boton1.Bind(EVT_BUTTON,self.CargarAnimal)
        self.boton1.Bind(EVT_ENTER_WINDOW, self.MO_1)
        self.boton1.Bind(wx.EVT_LEAVE_WINDOW, self.ML_1)

        self.boton2=Button(self.vent10,-1,label="",pos=(226,261),size=(250,45))
        self.boton2.SetBitmap(BitmapFromImage(Image("img/control_w.jpg")))
        self.boton2.Show()
        self.boton2.Bind(EVT_BUTTON,self.Controlar)
        self.boton2.Bind(EVT_ENTER_WINDOW, self.MO_2)
        self.boton2.Bind(wx.EVT_LEAVE_WINDOW, self.ML_2)

        self.boton3=Button(self.vent10,-1,label="",pos=(226,324),size=(250,45))
        self.boton3.SetBitmap(BitmapFromImage(Image("img/buscar_w.jpg")))
        self.boton3.Show()
        self.boton3.Bind(EVT_BUTTON, self.PestaBuscar)
        self.boton3.Bind(EVT_ENTER_WINDOW, self.MO_3)
        self.boton3.Bind(wx.EVT_LEAVE_WINDOW, self.ML_3)

        self.boton4=Button(self.vent10,-1,label="",pos=(226,387),size=(250,45))
        self.boton4.SetBitmap(BitmapFromImage(Image("img/ventas_w.jpg")))
        self.boton4.Show()
        self.boton4.Bind(EVT_BUTTON, self.PestaVentas)
        self.boton4.Bind(EVT_ENTER_WINDOW, self.MO_4)
        self.boton4.Bind(wx.EVT_LEAVE_WINDOW, self.ML_4)
#--------------------------------------------------------------------------------------------

#panel de control---------------------------------------------------------------------------
        self.panec=Panel(self.f0,-1,pos=(0,0),size=(1400,750))
        self.panec.SetBackgroundColour((255,0,0))

#panel donde esta la lista de control
        self.panellista=Panel(self.panec,-1,pos=(30,180),size=(1200,500))

#lista de control
        self.listacompleta=dv.DataViewListCtrl(self.panellista,pos=(0,0),size=(1100,500))
        encabezado = [('     Caravana', 150), ('F.Nac.', 150), ('Categoria', 150), ('Sexo', 150), ('Color', 150), ('Caravana madre', 100)]
        for enca in encabezado:
            self.listacompleta.AppendTextColumn(enca[0], width=enca[1])
        self.listacompleta.Show(False)
#--------------------------------------------------------------------------------------------


#panel de buscar----------------------------------------------------------------------------
        self.panelbuscar=Panel(self.f0,-1,pos=(0,0),size=(1400,800))
        self.panelbuscar.SetBackgroundColour((0,255,0))

#panel del imput
        self.panelbuscador=Panel(self.panelbuscar,-1,pos=(80,55),size=(400,110))
        grilla2 = GridBagSizer(0,2)

        textonurocarav=StaticText(self.panelbuscador, -1, "Ingrese numero a buscar: ")
        font = wx.Font(13, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        textonurocarav.SetFont(font)
        grilla2.Add(textonurocarav,pos=(0,0))

        self.ingresernero=TextCtrl(self.panelbuscador,-1,"")
        grilla2.Add(self.ingresernero,pos=(0,1))

        guardar = Button(self.panelbuscador, -1, "Buscar")
        grilla2.Add(guardar, pos = (0, 2))
        guardar.Bind(EVT_BUTTON, self.ObtenerResultadoBusqueda)
        self.panelbuscador.SetSizerAndFit(grilla2)

#panel de eliminar
        self.paneleliminar=Panel(self.panelbuscar,-1,pos=(80,650),size=(400,110))
        grilla2 = GridBagSizer(0,2)

        textonurocarav1=StaticText(self.paneleliminar, -1, "Ingrese numero para eliminar: ")
        font = wx.Font(13, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        textonurocarav1.SetFont(font)
        grilla2.Add(textonurocarav1,pos=(0,0))

        self.ingresernero2=TextCtrl(self.paneleliminar,-1,"")
        grilla2.Add(self.ingresernero2,pos=(0,1))

        eliminar = Button(self.paneleliminar, -1, "Eliminar")
        grilla2.Add(eliminar, pos = (0, 2))
        eliminar.Bind(EVT_BUTTON, self.Eliminar)
        self.paneleliminar.SetSizerAndFit(grilla2)

        self.panelbuscador.Show(False)
        self.paneleliminar.Show(False)



#--------------------------------------------------------------------------------------------

#panel de ventas---------------------------------------------------------------------------
        self.ventas=Panel(self.f0,-1,pos=(0,0),size=(1400,750))
        self.ventas.SetBackgroundColour((0,0,255))

#barra gris1
        self.barra=Panel(self.panec,-1,pos=(0,0),size=(1400,35))
        self.barra.SetBackgroundColour((80,80,80))
        self.barra.Refresh()
#barra gris2
        self.barra2=Panel(self.panelbuscar,-1,pos=(0,0),size=(1400,35))
        self.barra2.SetBackgroundColour((80,80,80))
        self.barra2.Refresh()
#barra gris2
        self.barra3=Panel(self.ventas,-1,pos=(0,0),size=(1400,35))
        self.barra3.SetBackgroundColour((80,80,80))
        self.barra3.Refresh()


#boton atras1
        self.boton1enbarra=Button(self.barra,-1,pos=(20,2),size=(30,30))
        self.boton1enbarra.SetBitmap(BitmapFromImage(Image("img/flechaatras.png")))
        self.boton1enbarra.Bind(EVT_BUTTON,self.IrAlMenu)
        self.boton1enbarra.Bind(EVT_ENTER_WINDOW, self.MO_F)
        self.boton1enbarra.Bind(wx.EVT_LEAVE_WINDOW, self.ML_F)
        self.boton1enbarra.Show(False)

        self.boton2enbarra=Button(self.barra2,-1,pos=(20,2),size=(30,30))
        self.boton2enbarra.SetBitmap(BitmapFromImage(Image("img/flechaatras.png")))
        self.boton2enbarra.Bind(EVT_BUTTON,self.IrAlMenu2)
        self.boton2enbarra.Bind(EVT_ENTER_WINDOW, self.MO_F2)
        self.boton2enbarra.Bind(wx.EVT_LEAVE_WINDOW, self.ML_F2)
        self.boton2enbarra.Show(False)

        self.boton3enbarra=Button(self.barra3,-1,pos=(20,2),size=(30,30))
        self.boton3enbarra.SetBitmap(BitmapFromImage(Image("img/flechaatras.png")))
        self.boton3enbarra.Bind(EVT_BUTTON,self.IrAlMenu3)
        self.boton3enbarra.Bind(EVT_ENTER_WINDOW, self.MO_F3)
        self.boton3enbarra.Bind(wx.EVT_LEAVE_WINDOW, self.ML_F3)
        self.boton3enbarra.Show(False)



        f0.Centre(True)
        f0.Show()
        return True

    def CargarAnimal(self,e):
        self.f1=f1 = Frame(None, -1, "Cargar nuevo animal", size = (375, 370))
        p2=self.p2=Panel(f1,-1,style=wx.TAB_TRAVERSAL)
        grilla = GridBagSizer(7,5)
        f1.Centre(True)
# Caravana - Caja de Texto
        l_ape=StaticText(p2,-1,"     Numero de Caravana:")
        grilla.Add(l_ape,pos=(1,0))
        caravana=self.caravana=TextCtrl(p2,-1,"")
        grilla.Add(caravana,pos=(1,1),span=(1,3))
        adi1 = self.adi1 = CheckBox(p2, -1, "No tiene")
        grilla.Add(adi1, pos = (2, 1))
# Fecha de Nacimiento - Caja de Texto con fecha de hoy - Abre calendario
        l_fna=StaticText(p2,-1,"     Fecha de Nacimiento:")
        grilla.Add(l_fna,pos=(3,0))
        hoy = str(DateTime.Today())
        hoy = hoy[3:5] + "/" + hoy[:2] + "/20" + hoy[6:8]
        print hoy
        self.fna = TextCtrl(p2, -1, hoy)
        self.fna.Bind(EVT_LEFT_DOWN, self.abrirCal)
        grilla.Add(self.fna, pos = (3,1), span = (1, 3))
# Clasificacion - Combo
        clasif= StaticText(p2, -1, "     Clasificacion:")
        grilla.Add(clasif, pos = (4,0))
        proList=["Toro","Vaca","Ternero","Novillito","Vaquillona"]
        self.cl=cl= ComboBox(p2, 500, "Clasificacion", (90, 50), (160, -1), proList, CB_DROPDOWN | TE_PROCESS_ENTER )
        self.Bind(EVT_COMBOBOX, self.EvtComboBox,cl)
        self.Bind(EVT_TEXT, self.EvtText,cl)
        self.Bind(EVT_TEXT_ENTER, self.EvtTextEnter,cl)
        cl.Bind(EVT_SET_FOCUS, self.OnSetFocus)
        cl.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        grilla.Add(self.cl, pos = (4,1), span = (1, 3))
# Sexo - Radio Buttons
        l_imp = StaticText(p2, -1, "     Sexo:")
        grilla.Add(l_imp, pos = (5,0))
        sexolist= ["Macho", "Hembra"]
        sexo= self.sexo= RadioBox(p2, -1, "", DefaultPosition, DefaultSize,sexolist, 1, NO_BORDER)
        grilla.Add(sexo, pos = (5, 1))
# Color - Combo
        l_pro = StaticText(p2, -1, "     Color:")
        grilla.Add(l_pro, pos = (6,0))
        proList = ["Colorado","Negro" , "Pampa colorado", "Pampa negro", "Holando"]
        self.color=color= ComboBox(p2, 500, " Color", (90, 50), (160, -1), proList, CB_DROPDOWN | TE_PROCESS_ENTER )
        self.Bind(EVT_COMBOBOX, self.EvtComboBox,color)
        self.Bind(EVT_TEXT, self.EvtText,color)
        self.Bind(EVT_TEXT_ENTER, self.EvtTextEnter,color)
        color.Bind(EVT_SET_FOCUS, self.OnSetFocus)
        color.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        grilla.Add(self.color, pos = (6,1), span = (1, 3))
# Caravana Madre - Caja de Texto
        l_nom=StaticText(p2,-1,"     Numero de Caravana de madre:")
        grilla.Add(l_nom,pos=(7,0))
        cara=self.cara=TextCtrl(p2,-1,"")
        grilla.Add(cara,pos=(7,1),span=(1,3))
        car2= self.car2= CheckBox(p2, -1, "No tiene")
        grilla.Add(car2, pos = (8,1))
# Botón Guardar
        guardar = Button(p2, -1, "Guardar")
        grilla.Add(guardar, pos = (9, 1))
        guardar.Bind(EVT_BUTTON, self.guardarAnimal)
# Muestra la grilla
        p2.SetSizerAndFit(grilla)
        f1.Show()

    def guardarAnimal(self, evt):

        adi1=self.adi1.GetValue()
        if adi1==False:
            car=self.caravana.GetValue()
        else:
            car="No tiene"
        fnac=self.fna.GetValue()
        clase=self.cl.GetValue()
        color=self.color.GetValue()
        sexo= self.sexo.GetString(self.sexo.GetSelection())
        cara=self.car2.GetValue()
        if cara==False:
            car2=self.cara.GetValue()
        else:
            car2="No tiene"
        self.f1.Show(False)
        unavaca=[car,fnac,clase,sexo,color,car2]
        print unavaca

        MiHacienda=open("Hacienda.csv","a")
        MiHacienda_c=csv.writer(MiHacienda)
        MiHacienda_c.writerow(unavaca)
        MiHacienda.close()

    def Controlar(self,a):
        self.panec.Show()
        self.vent10.Show(False)
        self.ventas.Show(False)
        self.panelbuscar.Show(False)
        self.boton1enbarra.Show()

        #PANEL DATOS


        self.paneldatos=Panel(self.panec,-1,pos=(335,50),size=(400,110))
        self.paneldatos.SetBackgroundColour((240,240,240))
        self.paneldatos.Refresh()

        self._d=wx.Image('img/informacion.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.boton1_d=wx.StaticBitmap(self.paneldatos,-1,self._d,pos=(110,0),size=(150,28))
        self.boton1_d.Show()

        Mitotalanimales=0
        Mitotalmachos=0
        Mitotalhembras=0
        Mitotaltoros=0
        Mitotalvacas=0
        Mitotalterneros=0
        Mitotalnovillos=0
        Mitotalvaquillonas=0
        Mitotalterneras=0

        miarchivo=open("Hacienda.csv","r")
        miarchivo_csv=csv.reader(miarchivo)
        for y in miarchivo_csv:
            x=str(y)
            Mitotalanimales=Mitotalanimales+1
            if "Macho" in x:
                Mitotalmachos=Mitotalmachos+1
            if "Hembra" in x:
                Mitotalhembras=Mitotalhembras+1
            if "Toro" in x:
                Mitotaltoros=Mitotaltoros+1
            if "Vaca" in x:
                Mitotalvacas=Mitotalvacas+1
            if "Ternero" in x and "Macho" in x:
                Mitotalterneros=Mitotalterneros+1
            if "Novillito" in x:
                Mitotalnovillos=Mitotalnovillos+1
            if "Vaquillona" in x:
                Mitotalvaquillonas=Mitotalvaquillonas+1
            if "Ternero" in x and "Hembra" in x:
                Mitotalterneras=Mitotalterneras+1
        miarchivo.close()
        self.Mitotalanimales=str(Mitotalanimales)
        self.Mitotalmachos=str(Mitotalmachos)
        self.Mitotalhembras=str(Mitotalhembras)
        self.Mitotaltoros=str(Mitotaltoros)
        self.Mitotalvacas=str(Mitotalvacas)
        self.Mitotalterneros=str(Mitotalterneros)
        self.Mitotalnovillos=str(Mitotalnovillos)
        self.Mitotalvaquillonas=str(Mitotalvaquillonas)
        self.Mitotalterneras=str(Mitotalterneras)

        self.paneltotales=Panel(self.paneldatos,-1,pos=(0,45),size=(200,140))
        grilla1 = GridBagSizer(2,5)



        totaltotal=StaticText(self.paneltotales, -1, "        Total animales: ")
        grilla1.Add(totaltotal, pos = (0,0))
        self.toti1=StaticText(self.paneltotales,-1,label=self.Mitotalanimales)
        grilla1.Add(self.toti1, pos = (0,1))

        totalmachos=StaticText(self.paneltotales, -1, "    Total machos: ")
        grilla1.Add(totalmachos, pos = (0,2))
        toti2=StaticText(self.paneltotales,-1,label=self.Mitotalmachos,style=wx.ALIGN_RIGHT)
        grilla1.Add(toti2, pos = (0,3))

        totalhembras=StaticText(self.paneltotales, -1, "    Total hembras: ")
        grilla1.Add(totalhembras, pos = (0,4))
        toti3=StaticText(self.paneltotales,-1,label=self.Mitotalhembras,style=wx.ALIGN_RIGHT)
        grilla1.Add(toti3, pos = (0,5))
#------------------------------------------------------------------------------
        totalterneros=StaticText(self.paneltotales, -1, "        Total terneros: ")
        grilla1.Add(totalterneros, pos = (1,0))
        toti4=StaticText(self.paneltotales,-1,label=self.Mitotalterneros,style=wx.ALIGN_RIGHT)
        grilla1.Add(toti4, pos = (1,1))

        totalterneras=StaticText(self.paneltotales, -1, "    Total terneras: ")
        grilla1.Add(totalterneras, pos = (1,2))
        toti4=StaticText(self.paneltotales,-1,label=self.Mitotalterneras,style=wx.ALIGN_RIGHT)
        grilla1.Add(toti4, pos = (1,3))

        totalnovillos=StaticText(self.paneltotales, -1, "    Total novillos: ")
        grilla1.Add(totalnovillos, pos = (2,4))
        toti5=StaticText(self.paneltotales,-1,label=self.Mitotalnovillos,style=wx.ALIGN_RIGHT)
        grilla1.Add(toti5, pos = (2,5))

        totalvaquillonas=StaticText(self.paneltotales, -1, "    Total vaquillonas: ")
        grilla1.Add(totalvaquillonas, pos = (1,4))
        toti6=StaticText(self.paneltotales,-1,label=self.Mitotalvaquillonas,style=wx.ALIGN_RIGHT)
        grilla1.Add(toti6, pos = (1,5))

        totaltoros=StaticText(self.paneltotales, -1, "        Total toros: ")
        grilla1.Add(totaltoros, pos = (2,0))
        toti7=StaticText(self.paneltotales,-1,label=self.Mitotaltoros,style=wx.ALIGN_RIGHT)
        grilla1.Add(toti7, pos = (2,1))

        totalvacas=StaticText(self.paneltotales, -1, "    Total vacas: ")
        grilla1.Add(totalvacas, pos = (2,2))
        toti8=StaticText(self.paneltotales,-1,label=self.Mitotalvacas,style=wx.ALIGN_RIGHT)
        grilla1.Add(toti8, pos = (2,3))

        self.paneltotales.SetSizerAndFit(grilla1)

        self.listacompleta=""

        self.listacompleta=dv.DataViewListCtrl(self.panellista,pos=(0,0),size=(1100,500))
        encabezado = [('     Caravana', 150), ('F.Nac.', 150), ('Categoria', 150), ('Sexo', 150), ('Color', 150), ('Caravana madre', 100)]
        for enca in encabezado:
            self.listacompleta.AppendTextColumn(enca[0], width=enca[1])

        miarchivo=open("Hacienda.csv","r")
        miarchivo_csv=csv.reader(miarchivo)
        for nro,fecha,categ,sexo,color,madre in miarchivo_csv:
            self.listacompleta.AppendItem([nro,fecha,categ,sexo,color,madre])
        miarchivo.close()
        self.listacompleta.Show(True)

    def PestaBuscar(self,a):
        self.panelbuscar.Show()
        self.vent10.Show(False)
        self.ventas.Show(False)
        self.panec.Show(False)
        self.boton2enbarra.Show()
        self.panelbuscador.Show()
        self.paneleliminar.Show()

#aca se muestran los resultados de las busquedas
        self.listacompleta2=dv.DataViewListCtrl(self.panelbuscar,pos=(50,100),size=(1100,500))
        encabezado = [('     Caravana', 150), ('F.Nac.', 150), ('Categoria', 150), ('Sexo', 150), ('Color', 150), ('Caravana madre', 100)]
        for enca in encabezado:
            self.listacompleta2.AppendTextColumn(enca[0], width=enca[1])
        self.listacompleta2.Show()

    def ObtenerResultadoBusqueda(self,a):
        self.ListaResultados=[]
        buscar=self.ingresernero.GetValue()
        miarchivo=open("Hacienda.csv","r")
        miarchivo_csv=csv.reader(miarchivo)
        for nro,fecha,categ,sexo,color,madre in miarchivo_csv:
            if (buscar==nro) or (buscar in nro):
                print "resultado:",nro,fecha,categ,sexo,color,madre
                self.ListaResultados.Add(nro)
                #self.listacompleta2.AppendItem([nro,fecha,categ,sexo,color,madre])
                print self.ListaResultados
        self.listacompleta2.Refresh(True)
        miarchivo.close()

    def Eliminar(self,a):
        eliminar=self.ingresernero2.GetValue()
        miarchivo=open("Hacienda.csv","r")
        miarchivo_csv=csv.reader(miarchivo)
        print eliminar
        miarchivo_csv.remove(eliminar)
        miarchivo.close()


    def PestaVentas(self,a):
        self.ventas.Show()
        self.vent10.Show(False)
        self.panec.Show(False)
        self.panelbuscar.Show(False)
        self.boton3enbarra.Show()

    def IrAlMenu(self,a):
        self.vent10.Show()
        self.panec.Show(False)

    def IrAlMenu2(self,a):
        self.vent10.Show()
        self.panelbuscar.Show(False)

    def IrAlMenu3(self,a):
        self.vent10.Show()
        self.ventas.Show(False)

    def MO_1(self, event):
        self._d=wx.Image('img/cargar_d.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.boton1_d=wx.StaticBitmap(self.vent10,-1,self._d,pos=(226,200),size=(252,47))
        self.boton1_d.Show()
    def MO_2(self, event):
        self._d=wx.Image('img/control_d.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.boton2_d=wx.StaticBitmap(self.vent10,-1,self._d,pos=(226,261),size=(252,47))
        self.boton2_d.Show()
    def MO_3(self, event):
        self._d=wx.Image('img/buscar_d.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.boton3_d=wx.StaticBitmap(self.vent10,-1,self._d,pos=(226,324),size=(252,47))
        self.boton3_d.Show()
    def MO_4(self, event):
        self._d=wx.Image('img/ventas_d.jpg',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.boton4_d=wx.StaticBitmap(self.vent10,-1,self._d,pos=(226,387),size=(252,47))
        self.boton4_d.Show()
    def MO_F(self, event):
        self._d=wx.Image('img/flechaatras_w.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.boton1enbarra=wx.StaticBitmap(self.barra,-1,self._d,pos=(20,2),size=(30,30))
        self.boton1enbarra.Show()
    def MO_F2(self,a):
        self._d=wx.Image('img/flechaatras_w.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.boton2enbarra=wx.StaticBitmap(self.barra2,-1,self._d,pos=(20,2),size=(30,30))
        self.boton2enbarra.Show()
    def MO_F3(self,a):
        self._d=wx.Image('img/flechaatras_w.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.boton3enbarra=wx.StaticBitmap(self.barra3,-1,self._d,pos=(20,2),size=(30,30))
        self.boton3enbarra.Show()

    def ML_1(self, event):
        self.boton1_d.Show(False)
    def ML_2(self, event):
        self.boton2_d.Show(False)
    def ML_3(self, event):
        self.boton3_d.Show(False)
    def ML_4(self, event):
        self.boton4_d.Show(False)
    def ML_F(self, event):
        self.boton1enbarra.Show(False)
    def ML_F2(self,a):
        self.boton2enbarra.Show(False)
    def ML_F3(self,a):
        self.boton3enbarra.Show(False)

# Begin Combo
    def OnSetFocus(self, evt):
        print "OnSetFocus"
        evt.Skip()
    def OnKillFocus(self, evt):
        print "OnKillFocus"
        evt.Skip()
    def EvtComboBox(self, evt):
        cb = evt.GetEventObject()
        data = cb.GetClientData(evt.GetSelection())
        print('EvtComboBox: %s\nClientData: %s\n' % (evt.GetString(), data))

        if evt.GetString() == 'one':
            print("You follow directions well!\n\n")
    def EvtText(self, evt):
        print('EvtText: %s\n' % evt.GetString())
        evt.Skip()
    def EvtTextEnter(self, evt):
        print('EvtTextEnter: %s' % evt.GetString())
        evt.Skip()

# End Combo

# Begin Calendario
    def abrirCal(self, e):
        self.f3 = Frame(None, -1, "Calendario")
        g3 = GridSizer(0,0)
        cal = calendar.CalendarCtrl(self.f3, -1, DateTime.Today(), style=calendar.CAL_SEQUENTIAL_MONTH_SELECTION)
        g3.Add(cal)
        cal.Bind(calendar.EVT_CALENDAR, self.OnCalSelected)
        self.f3.SetSizerAndFit(g3)
        self.f3.Show()
    def OnCalSelected(self, e):
        #print('OnCalSelected: %s\n' % e.GetDate())
        hoy = str(e.GetDate())
        hoy = hoy[3:5] + "/" + hoy[:2] + "/20" + hoy[6:8]
        self.f3.Show(False)
        self.fna.SetValue(hoy)

prog = MiApp()
prog.MainLoop()