from rest_framework import viewsets, response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import json
from django.shortcuts import get_object_or_404
from .models import viviendas
from .serializer import ViviendaSerializer

class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = viviendas.objects.all
    serializer_class = ViviendaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo']

class ViviendaList(viewsets.ModelViewSet):
    def list(self, request):
        #id de la vivienda
        idViviendaVar = request.query_params.get('idVivienda')
        queryset = viviendas.objects.filter()
        serializer_class =  ViviendaSerializer(queryset, many=True)
        return response(serializer_class)
    
def listar_viviendas(request):
    viviendas = viviendas.objects.all()  
    data = {
        'viviendas': viviendas,
    }
    return render(request, 'portaView/src/views/?', data)

def registrar_propiedad(request):
    if request.method == 'POST':

        propiedad_vivienda = viviendas.objects.create(
            fechaInicio=request.POST.get('fecha_inicio'),
            fechaTermino=request.POST.get('fecha_termino'),
            empresa=request.POST.get('empresa'),
            agente=request.POST.get('agente'),
            ocultarDir=request.POST.get('ocultar_dir'),
            exclusivo=request.POST.get('exclusivo'),
            titulo=request.POST.get('titulo'),
            cometario=request.POST.get('comentario'),
            tipoVivienda=request.POST.get('tipo_vivienda'),
            usoActual=request.POST.get('uso_actual'),
            usoPermitido=request.POST.get('uso_permitido'),
            condicionFisica=request.POST.get('condicion_fisica'),
            precioVenta=request.POST.get('precio_venta'),
            precioRenta=request.POST.get('precio_renta'),
            precioMinimo=request.POST.get('precio_minimo'),
            precioPromedio=request.POST.get('precio_promedio'),
            precioMaximo=request.POST.get('precio_maximo'),
            comision1=request.POST.get('comision1'),
            ganancia1=request.POST.get('ganancia1'),
            comision2=request.POST.get('comision2'),
            ganancia2=request.POST.get('ganancia2'),
            disponibilidad=request.POST.get('disponibilidad'),
            claseInmueble=request.POST.get('clase_inmueble'),
            numeroFrentes=request.POST.get('numero_frentes'),
            medidaTerreno=request.POST.get('medida_terreno'),
            m2Terreno=request.POST.get('m2_terreno'),
            construccionN1=request.POST.get('construccion_n1'),
            construccionN2=request.POST.get('construccion_n2'),
            construccionN3=request.POST.get('construccion_n3'),
            gravamen=request.POST.get('gravamen'),
            valorGravamen=request.POST.get('valor_gravamen'),
            valorSegunAvaluo=request.POST.get('valor_segun_avaluo'),
            operacion=request.POST.get('operacion'),
            condicionPago=request.POST.get('condicion_pago'),
            aceptaInfonavit=request.POST.get('acepta_infonavit'),
            aceptaFovisste=request.POST.get('acepta_fovisste'),
            propietario=request.POST.get('propietario'),
            claveCastratal=request.POST.get('clave_catastral'),
            lote=request.POST.get('lote'),
            manzana=request.POST.get('manzana'),
            cuentaAgua=request.POST.get('cuenta_agua'),
            autosEst=request.POST.get('autos_est'),
            autosIndep=request.POST.get('autos_indep'),
            estacionamiento=request.POST.get('estacionamiento'),
            cocheraElectrica=request.POST.get('cochera_electrica'),
            patio=request.POST.get('patio'),
            asador=request.POST.get('asador'),
            fuentes=request.POST.get('fuentes'),
            jacuzzi=request.POST.get('jacuzzi'),
            alberca=request.POST.get('alberca'),
            jardin=request.POST.get('jardin'),
            bodega=request.POST.get('bodega'),
            cisterna=request.POST.get('cisterna'),
            tinaco=request.POST.get('tinaco'),
            acCentral=request.POST.get('ac_central'),
            proteccionVentana=request.POST.get('proteccion_ventana'),
            persianaCortina=request.POST.get('persiana_cortina'),
            hidroneumatico=request.POST.get('hidroneumatico'),
            amueblado=request.POST.get('amueblado'),
            piso1=request.POST.get('piso1'),
            piso2=request.POST.get('piso2'),
            piso3=request.POST.get('piso3'),
            alarma=request.POST.get('alarma'),
            uriGoogleMaps=request.POST.get('uri_google_maps'),
            cocinaIntegral=request.POST.get('cocina_integral'),
            vitropiso=request.POST.get('vitropiso'),
            closet=request.POST.get('closet'),
            barda=request.POST.get('barda'),
            patioEncementado=request.POST.get('patio_encementado'),
            equipada=request.POST.get('equipada'),
            pais=request.POST.get('pais'),
            estado=request.POST.get('estado'),
            municipio=request.POST.get('municipio'),
            ciudad=request.POST.get('ciudad'),
            colonia=request.POST.get('colonia'),
            codigoPostal=request.POST.get('codigo_postal'),
            calle=request.POST.get('calle'),
            numExterior=request.POST.get('num_exterior'),
            numInterior=request.POST.get('num_interior'),
            entreCalle1=request.POST.get('entre_calle1'),
            entreCalle2=request.POST.get('entre_calle2'),
            nombreComplejo=request.POST.get('nombre_complejo'),
            escrituracion=request.POST.get('escrituracion'),
            avaluo=request.POST.get('avaluo'),
            impuestos=request.POST.get('impuestos'),
            otros=request.POST.get('otros'),
            total=request.POST.get('total'),
            imagen=request.POST.get('imagen')
        )

        
        propiedad_vivienda.save()

        messages.success(
            request, f"Felicitaciones, la propiedad vivienda fue registrada correctamente")

    return redirect('portaView/src/views/?')

def editar_propiedad(request, id):
    try:
        if request.method == "POST":
            
            propiedad= viviendas.objects.get(id=id)

            propiedad.fechaInicio=request.POST.get('fecha_inicio'),
            propiedad.fechaTermino=request.POST.get('fecha_termino'),
            propiedad.empresa=request.POST.get('empresa'),
            propiedad.agente=request.POST.get('agente'),
            propiedad.ocultarDir=request.POST.get('ocultar_dir'),
            propiedad.exclusivo=request.POST.get('exclusivo'),
            propiedad.titulo=request.POST.get('titulo'),
            propiedad.cometario=request.POST.get('comentario'),
            propiedad.tipoVivienda=request.POST.get('tipo_vivienda'),
            propiedad.usoActual=request.POST.get('uso_actual'),
            propiedad.usoPermitido=request.POST.get('uso_permitido'),
            propiedad.condicionFisica=request.POST.get('condicion_fisica'),
            propiedad.precioVenta=request.POST.get('precio_venta'),
            propiedad.precioRenta=request.POST.get('precio_renta'),
            propiedad.precioMinimo=request.POST.get('precio_minimo'),
            propiedad.precioPromedio=request.POST.get('precio_promedio'),
            propiedad.precioMaximo=request.POST.get('precio_maximo'),
            propiedad.comision1=request.POST.get('comision1'),
            propiedad.ganancia1=request.POST.get('ganancia1'),
            propiedad.comision2=request.POST.get('comision2'),
            propiedad.ganancia2=request.POST.get('ganancia2'),
            propiedad.disponibilidad=request.POST.get('disponibilidad'),
            propiedad.claseInmueble=request.POST.get('clase_inmueble'),
            propiedad.numeroFrentes=request.POST.get('numero_frentes'),
            propiedad.medidaTerreno=request.POST.get('medida_terreno'),
            propiedad.m2Terreno=request.POST.get('m2_terreno'),
            propiedad.construccionN1=request.POST.get('construccion_n1'),
            propiedad.construccionN2=request.POST.get('construccion_n2'),
            propiedad.construccionN3=request.POST.get('construccion_n3'),
            propiedad.gravamen=request.POST.get('gravamen'),
            propiedad.valorGravamen=request.POST.get('valor_gravamen'),
            propiedad.valorSegunAvaluo=request.POST.get('valor_segun_avaluo'),
            propiedad.operacion=request.POST.get('operacion'),
            propiedad.condicionPago=request.POST.get('condicion_pago'),
            propiedad.aceptaInfonavit=request.POST.get('acepta_infonavit'),
            propiedad.aceptaFovisste=request.POST.get('acepta_fovisste'),
            propiedad.propietario=request.POST.get('propietario'),
            propiedad.claveCastratal=request.POST.get('clave_catastral'),
            propiedad.lote=request.POST.get('lote'),
            propiedad.manzana=request.POST.get('manzana'),
            propiedad.cuentaAgua=request.POST.get('cuenta_agua'),
            propiedad.autosEst=request.POST.get('autos_est'),
            propiedad.autosIndep=request.POST.get('autos_indep'),
            propiedad.estacionamiento=request.POST.get('estacionamiento'),
            propiedad.cocheraElectrica=request.POST.get('cochera_electrica'),
            propiedad.patio=request.POST.get('patio'),
            propiedad.asador=request.POST.get('asador'),
            propiedad.fuentes=request.POST.get('fuentes'),
            propiedad.jacuzzi=request.POST.get('jacuzzi'),
            propiedad.alberca=request.POST.get('alberca'),
            propiedad.jardin=request.POST.get('jardin'),
            propiedad.bodega=request.POST.get('bodega'),
            propiedad.cisterna=request.POST.get('cisterna'),
            propiedad.tinaco=request.POST.get('tinaco'),
            propiedad.acCentral=request.POST.get('ac_central'),
            propiedad.proteccionVentana=request.POST.get('proteccion_ventana'),
            propiedad.persianaCortina=request.POST.get('persiana_cortina'),
            propiedad.hidroneumatico=request.POST.get('hidroneumatico'),
            propiedad.amueblado=request.POST.get('amueblado'),
            propiedad.piso1=request.POST.get('piso1'),
            propiedad.piso2=request.POST.get('piso2'),
            propiedad.piso3=request.POST.get('piso3'),
            propiedad.alarma=request.POST.get('alarma'),
            propiedad.uriGoogleMaps=request.POST.get('uri_google_maps'),
            propiedad.cocinaIntegral=request.POST.get('cocina_integral'),
            propiedad.vitropiso=request.POST.get('vitropiso'),
            propiedad.closet=request.POST.get('closet'),
            propiedad.barda=request.POST.get('barda'),
            propiedad.patioEncementado=request.POST.get('patio_encementado'),
            propiedad.equipada=request.POST.get('equipada'),
            propiedad.pais=request.POST.get('pais'),
            propiedad.estado=request.POST.get('estado'),
            propiedad.municipio=request.POST.get('municipio'),
            propiedad.ciudad=request.POST.get('ciudad'),
            propiedad.colonia=request.POST.get('colonia'),
            propiedad.codigoPostal=request.POST.get('codigo_postal'),
            propiedad.calle=request.POST.get('calle'),
            propiedad.numExterior=request.POST.get('num_exterior'),
            propiedad.numInterior=request.POST.get('num_interior'),
            propiedad.entreCalle1=request.POST.get('entre_calle1'),
            propiedad.entreCalle2=request.POST.get('entre_calle2'),
            propiedad.nombreComplejo=request.POST.get('nombre_complejo'),
            propiedad.escrituracion=request.POST.get('escrituracion'),
            propiedad.avaluo=request.POST.get('avaluo'),
            propiedad.impuestos=request.POST.get('impuestos'),
            propiedad.otros=request.POST.get('otros'),
            propiedad.total=request.POST.get('total'),
            propiedad.imagen=request.POST.get('imagen')
            
            
            propiedad.save()
            
            return redirect('portaView/src/views/?')
    except ObjectDoesNotExist:
        error_message = f"La propiedad vivienda con id: {id} no se actualizó."
        return render(request, "portaView/src/views/?", {"error_message": error_message})
    
def eliminar_propiedad(request):
    if request.method == 'POST':
        idPropiedad = json.loads(request.body)['id']
        
        propiedad = get_object_or_404(viviendas, id=idPropiedad)
        
        propiedad.delete()
        return JsonResponse({'resultado': 1})
    return JsonResponse({'resultado': 0})