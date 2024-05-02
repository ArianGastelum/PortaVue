<template>
    <div class="decoration-line"></div>
    <body>
    <form @submit.prevent="createVivienda" name="solucionFormulario">
    <!-- ######### Seccion de fechas ######## -->
    <section>
    <h3>Fechas</h3>      
	<label for="fechaInicio">Fecha Inicio:</label>
	<input type="date" id="fechaInicio" name="fechaInicio" v-model="vivienda.fechaInicio">

	<label for="fechaFin">Fecha Fín:</label>
	<input type="date" id="fechaFin" name="fechaFin" v-model="vivienda.fechaFin">
    </section>
    
     <!-- ######### seccion de informacion de la propiedad ######## -->
    <section>
    <h3>Información de la propiedad:</h3>      
	<label for="titulo">Título:</label>
	<input type="text" id="titulo" name="titulo" placeholder="Escribe el título de la propiedad" maxlength="80" v-model="vivienda.titulo">

	<label for="comentario">Comentario:</label>
	<textarea name="comentario" id="comentario" maxlength="800" v-model="vivienda.comentario"></textarea>
    
    <label for="tipoVivienda">Tipo de vivienda:</label>
    <select name="tipoVivienda" id="tipoVivienda" v-model="vivienda.tipoVivienda">
      <option value="Departamento">Departamento</option>
      <option value="Vivienda">Vivienda</option>
    </select>

    <label for="usoActual">Uso Actual:</label>
	<input type="text" id="usoActual" name="usoActual" placeholder="Escribe el uso actual de la propiedad" maxlength="80" v-model="vivienda.usoActual">

    <label for="usoPermitido">Uso Permitido:</label>
	<input type="text" id="usoPermitido" name="usoPermitido" placeholder="Escribe el uso permitido de la propiedad" maxlength="80" v-model="vivienda.usoPermitido">

    <label for="condicionFisica">Condición Física:</label>
	<textarea name="condicionFisica" id="condicionFisica" maxlength="800" v-model="vivienda.condicionFisica"></textarea>

    <label for="claseInmueble">Clase de Inmueble:</label>
	<input type="text" id="claseInmueble" name="claseInmueble" placeholder="Escribe la clase de inmueble de la propiedad" maxlength="80" v-model="vivienda.claseInmueble">

    <label for="numeroFrentes">Número de Frentes:</label>
	<input type="number" id="numeroFrentes" name="numeroFrentes" v-model="vivienda.numeroFrentes">

    <label for="medidaTerreno">Medida del Terreno:</label>
	<input type="text" id="medidaTerreno" name="medidaTerreno" placeholder="Escribe la medida de la propiedad" maxlength="80" v-model="vivienda.medidaTerreno">

    <label for="m2Terreno">M2 del Terreno:</label>
	<input type="text" id="m2Terreno" name="m2Terreno" placeholder="Escribe los m2 de la propiedad" maxlength="80" v-model="vivienda.m2Terreno">

    <label for="construccionN1">Construccion N1:</label>
	<input type="text" id="construccionN1" name="construccionN1" placeholder="8" maxlength="80" v-model="vivienda.construccionN1">

    <label for="construccionN2">Construccion N2:</label>
	<input type="text" id="construccionN2" name="construccionN2" placeholder="8" maxlength="80" v-model="vivienda.construccionN2">
    
    <label for="construccionN3">Construccion N3:</label>
	<input type="text" id="construccionN3" name="construccionN3" placeholder="8" maxlength="80" v-model="vivienda.construccionN3">

    <label for="gravamen">Gravamen:</label>
	<input type="text" id="gravamen" name="gravamen" placeholder="8" maxlength="80" v-model="vivienda.gravamen">
     <!-- ######### En duda ######## -->
    <label for="valorGravamen">Valor de Gravamen:</label>
	<input type="text" id="valorGravamen" name="valorGravamen" placeholder="Escribe el valor del gravamen" maxlength="80" v-model="vivienda.valorGravamen">

    <label for="valorAvaluo">Valor segun Avaúo:</label>
	<input type="text" id="valorAvaluo" name="valorAvaluo" placeholder="Escribe el valor segun avalúo" maxlength="80" v-model="vivienda.valorAvaluo">

    <label for="operacion">Operación:</label>
	<input type="text" id="operacion" name="operacion" placeholder="Escribe la operacion" maxlength="80" v-model="vivienda.operacion">

    <label for="condicionPago">Condición de Pago:</label>
	<input type="text" id="condicionPago" name="condicionPago" placeholder="Escribe la condición de pago" maxlength="80" v-model="vivienda.condicionPago">

    <label for="escrituracion">Escrituración:</label>
	<input type="text" id="escrituracion" name="escrituracion" placeholder="Escribe la escrituración" maxlength="80" v-model="vivienda.escrituracion">

    <label for="avaluo">Avalúo:</label>
	<input type="text" id="avaluo" name="avaluo" placeholder="Escribe el avalúo de la propiedad" maxlength="80"v-model="vivienda.avaluo">

    <label for="impuestos">Impuestos:</label>
	<input type="text" id="impuestos" name="impuestos" placeholder="Escribe el avalúo de la propiedad" maxlength="80" v-model="vivienda.impuestos">

    <label for="otros">Otros:</label>
	<textarea name="otros" id="otros" maxlength="400" v-model="vivienda.otros"></textarea>

    <label for="total">Total:</label>
	<input type="text" id="total" name="total" placeholder="Escribe el avalúo de la propiedad" maxlength="80" v-model="vivienda.total">
    </section>
    
    <!-- ######### seccion de precios y comisiones ######## -->
    <section>
    <h3>Precios y comisiones</h3>
    <label for="precioVenta">Precio de  Venta:</label>
	<input type="text" id="precioVenta" name="precioVenta" placeholder="Escribe el precio de venta de la propiedad" maxlength="80" v-model="vivienda.precioVenta">

    <label for="precioRenta">Precio de Renta:</label>
	<input type="text" id="precioRenta" name="precioRenta" placeholder="Escribe el precio de renta de la propiedad" maxlength="80"v-model="vivienda.precioRenta">

    <label for="precioMinimo">Precio Minimo:</label>
	<input type="text" id="precioMinimo" name="precioMinimo" placeholder="Escribe el precio minimo de la propiedad" maxlength="80" v-model="vivienda.precioMinimo">

    <label for="precioPromedio">Precio Promedio:</label>
	<input type="text" id="precioPromedio" name="precioPromedio" placeholder="Escribe el precio promedio de la propiedad" maxlength="80" v-model="vivienda.precioPromedio">

    <label for="precioMaximo">Precio Maximo:</label>
	<input type="text" id="precioMaximo" name="precioMaximo" placeholder="Escribe el precio maximo de la propiedad" maxlength="80" v-model="vivienda.precioMaximo">
    
    <label for="comision1">Comision1:</label>
	<input type="text" id="comision1" name="comision1" placeholder="Escribe la comision de la propiedad" maxlength="80" v-model="vivienda.comision1">

    <label for="ganancia1">Ganancia1:</label>
	<input type="text" id="ganancia1" name="ganancia1" placeholder="Escribe la ganancia de la propiedad" maxlength="80" v-model="vivienda.ganancia1">
    
    <label for="comision2">Comision2:</label>
	<input type="text" id="comision2" name="comision2" placeholder="Escribe la comision de la propiedad" maxlength="80" v-model="vivienda.comision2">

    <label for="ganancia2">Ganancia2:</label>
	<input type="text" id="ganancia2" name="ganancia2" placeholder="Escribe la ganancia de la propiedad" maxlength="80" v-model="vivienda.ganancia2">
    </section>

    <!-- ######### seccion de la disponibilidad y exclusividad ######## -->
    <section>
    <h3>Disponibilidad y exclusividad</h3>
    <select name="tipoDisponibilidad" id="tipoDisponibilidad" v-model="vivienda.tipoDisponibilidad">
        <option value="Disponibilidad">Disponibilidad</option>
        <option value="Exclusividad">Exclusividad</option>
    </select>    
    </section>
    <!-- ######### seccion de la transaccion de la propiedad ######## -->
    <section>
    <h3>Información de la transacción de la propiedad</h3>
    <label for="empresa">Empresa:</label>
    <input type="text" id="empresa" name="empresa" maxlength="60" v-model="vivienda.empresa">

    <label for="agente">Agente:</label>
    <input type="text" id="agente" name="agente" maxlength="50" v-model="vivienda.agente">

    <label for="propietario">Propietario:</label>
    <input type="text" id="propietario" name="propietario" maxlength="80" v-model="vivienda.propietario">

    <label for="claveCastratal">Clave Catastral:</label>
    <input type="text" id="claveCastratal" name="claveCastratal" maxlength="30" v-model="vivienda.claveCastratal">

    <label for="lote">Lote:</label>
    <input type="text" id="lote" name="lote" maxlength="30" v-model="vivienda.lote">

    <label for="manzana">Manzana:</label>
    <input type="text" id="manzana" name="manzana" maxlength="30" v-model="vivienda.manzana">

    <label for="cuentaAgua">Cuenta de Agua:</label>
    <input type="checkbox" id="cuentaAgua" name="cuentaAgua" v-model="vivienda.cuentaAgua">

    <label for="ocultarDir">Ocultar Dirección:</label>
	<input type="checkbox" id="ocultarDir" name="ocultarDir" v-model="vivienda.ocultarDir">

    <label for="aceptaInfonavid">Acepta Infonavit:</label>
	<input type="checkbox" id="aceptaInfonavid" name="aceptaInfonavid" v-model="vivienda.aceptaInfonavid">

    <label for="aceptaFovisste">Acepta Fovisste:</label>
	<input type="checkbox" id="aceptaFovisste" name="aceptaFovisste" v-model="vivienda.aceptaFovisste">

    <label for="autosEst">Autos Estacionados:</label>
    <input type="number" id="autosEst" name="autosEst" min="0" max="10" v-model="vivienda.autosEst">

    <label for="autosIndep">Autos Independientes:</label>
    <input type="number" id="autosIndep" name="autosIndep" min="0" max="10" v-model="vivienda.autosIndep">

    <label for="estacionamiento">Estacionamiento:</label>
    <input type="text" id="estacionamiento" name="estacionamiento" maxlength="30" v-model="vivienda.estacionamiento">

    <label for="cocheraElectrica">Cochera Eléctrica:</label>
    <input type="text" id="cocheraElectrica" name="cocheraElectrica" v-model="vivienda.cocheraElectrica">

    <label for="patio">Patio:</label>
    <input type="text" id="patio" name="patio" maxlength="30" v-model="vivienda.patio">

    <label for="asador">Asador:</label>
    <input type="text" id="asador" name="asador" maxlength="70" v-model="vivienda.asador">

    <label for="fuentes">Fuentes:</label>
    <input type="text" id="fuentes" name="fuentes" maxlength="90" v-model="vivienda.fuentes">

    <label for="jacuzzi">Jacuzzi:</label>
    <input type="text" id="jacuzzi" name="jacuzzi" maxlength="120" v-model="vivienda.jacuzzi">

    <label for="alberca">Alberca:</label>
    <input type="text" id="alberca" name="alberca" maxlength="70" v-model="vivienda.alberca">

    <label for="jardin">Jardín:</label>
    <input type="text" id="jardin" name="jardin" maxlength="30" v-model="vivienda.jardin">

    <label for="bodega">Bodega:</label>
    <input type="text" id="bodega" name="bodega" maxlength="50" v-model="vivienda.bodega">

    <label for="cisterna">Cisterna:</label>
    <input type="text" id="cisterna" name="cisterna" maxlength="45" v-model="vivienda.cisterna">

    <label for="tinaco">Tinaco:</label>
    <input type="text" id="tinaco" name="tinaco" maxlength="45" v-model="vivienda.tinaco">

    <label for="acCentral">Aire Central:</label>
    <input type="checkbox" id="acCentral" name="acCentral" v-model="vivienda.acCentral">

    <label for="proteccionVentana">Protección de Ventana:</label>
    <input type="checkbox" id="proteccionVentana" name="proteccionVentana" v-model="vivienda.proteccionVentana">

    <label for="persianaCortina">Persiana Cortina:</label>
    <input type="checkbox" id="persianaCortina" name="persianaCortina" v-model="vivienda.persianaCortina">

    <label for="hidroneumatico">Hidroneumático:</label>
    <input type="checkbox" id="hidroneumatico" name="hidroneumatico" v-model="vivienda.hidroneumatico">

    <label for="patioEncementado">Patio Encementado:</label>
    <input type="checkbox" id="patioEncementado" name="patioEncementado" v-model="vivienda.patioEncementado">

    <label for="cocinaIntegral">Cocina integral:</label>
    <input type="text" id="cocinaIntegral" name="cocinaIntegral" maxlength="45" v-model="vivienda.CocinaIntegral">

    <label for="amueblado">Amueblado:</label>
    <input type="checkbox" id="amueblado" name="amueblado" v-model="vivienda.amueblado">

    <label for="piso1">Piso 1:</label>
    <input type="text" id="piso1" name="piso1" maxlength="30" v-model="vivienda.piso1">

    <label for="piso2">Piso 2:</label>
    <input type="text" id="piso2" name="piso2" maxlength="30"v-model="vivienda.piso2">

    <label for="piso3">Piso 3:</label>
    <input type="text" id="piso3" name="piso3" maxlength="30"v-model="vivienda.piso3">

    <label for="alarma">Alarma:</label>
    <input type="checkbox" id="alarma" name="alarma" v-model="vivienda.alarma">

    <label for="urlGoogleMap">URL Google Maps:</label>
    <input type="text" id="urlGoogleMap" name="urlGoogleMap" maxlength="150" v-model="vivienda.urlGoogleMap">

    <label for="vitropiso">Tipo de Vitropiso:</label>
    <input type="text" id="vitropiso" name="vitropiso" maxlength="80" v-model="vivienda.vitropiso">

    <label for="closet">Closet:</label>
    <input type="text" id="closet" name="closet" maxlength="30" v-model="vivienda.closet">

    <label for="barda">Barda:</label>
    <input type="text" id="barda" name="barda" maxlength="30" v-model="vivienda.barda">

    <label for="equipada">Equipada:</label>
    <input type="text" id="equipada" name="equipada" maxlength="30" v-model="vivienda.equipada">
    </section>
        
    <!-- ######### seccion de la ubicacion ######## -->
    <section>
    <h3>Ubicación</h3>      
    <label for="pais">País:</label>
    <input type="text" id="pais" name="pais" maxlength="30" v-model="vivienda.pais">

    <label for="estado">Estado:</label>
    <input type="text" id="estado" name="estado" maxlength="30" v-model="vivienda.estado">

    <label for="municipio">Municipio:</label>
    <input type="text" id="municipio" name="municipio" maxlength="30" v-model="vivienda.municipio">

    <label for="ciudad">Ciudad:</label>
    <input type="text" id="ciudad" name="ciudad" maxlength="30" v-model="vivienda.ciudad">

    <label for="colonia">Colonia:</label>
    <input type="text" id="colonia" name="colonia"   maxlength="30" v-model="vivienda.colonia">

    <label for="codigoPostal">Código Postal:</label>
    <input type="text" id="codigoPostal" name="codigoPostal"   maxlength="30" v-model="vivienda.codigoPostal">

    <label for="calle">Calle:</label>
    <input type="text" id="calle" name="calle"  maxlength="30" v-model="vivienda.calle">

    <label for="numExterior">Número Exterior:</label>
    <input type="text" id="numExterior" name="numExterior" maxlength="30" v-model="vivienda.numExterior">

    <label for="numInterior">Número Interior:</label>
    <input type="text" id="numInterior" name="numInterior"  maxlength="30" v-model="vivienda.numInterior">

    <label for="entreCalle1">Entre calle 1:</label>
    <input type="text" id="entreCalle1" name="entreCalle1"   maxlength="50" v-model="vivienda.entreCalle1">

    <label for="entreCalle2">Entre calle 2:</label>
    <input type="text" id="entreCalle2" name="entreCalle2"   maxlength="50" v-model="vivienda.entreCalle2">

    <label for="nombreComplejo">Nombre Complejo:</label>
    <input type="text" id="nombreComplejo" name="nombreComplejo"   maxlength="60" v-model="vivienda.nombreComplejo">
    </section>

    <!-- ######### seccion de la imagen ######## -->
    <section>
    <label for="imagen">Ingrese las imagenes de la vivienda:</label>
    <input type="file" id="imagen" name="imagen" accept="image/png, image/jpeg" multiple @change="vivienda.imagenes"/>
    </section>

    <button type="submit" class="button-primary">Crear vivienda</button>

</form>
</body>
</template>
<script>
//import axios from 'axios';
    export default{
        name:"CreateFormView",
        data:()=>{
            return{
                vivienda:{
                    fechaInicio: "",
                    fechaFin: "",
                    empresa: "",
                    agente: "",
                    ocultarDir: "",
                    exclusivo: "",
                    titulo: "",
                    comentario: "",
                    tipoVivienda: "",
                    usoActual: "",
                    usoPermitido: "",
                    condicionFisica: "",
                    precioVenta: "",
                    precioRenta: "",
                    precioMinimo: "",
                    precioPromedio: "",
                    precioMaximo: "",
                    comision1: "",
                    ganancia1: "",
                    comision2: "",
                    ganancia2: "",
                    disponibilidad: "",
                    claseInmueble: "",
                    numeroFrentes: "",
                    medidaTerreno: "",
                    m2Terreno: "",
                    construccionN1: "",
                    construccionN2: "",
                    construccionN3: "",
                    gravamen: "",
                    valorGravamen: "",
                    valorAvaluo: "",
                    operacion: "",
                    condicionPago: "",
                    aceptaInfonavit: "",
                    aceptaFovisste: "",
                    propietario: "",
                    claveCastratal: "",
                    lote: "",
                    manzana: "",
                    cuentaAgua: "",
                    autosEst: "",
                    autosIndep: "",
                    estacionamiento: "",
                    cocheraElectrica: "",
                    patio: "",
                    asador: "",
                    fuentes: "",
                    jacuzzi: "",
                    alberca: "",
                    jardin: "",
                    bodega: "",
                    cisterna: "",
                    tinaco: "",
                    acCentral: "",
                    proteccionVentana: "",
                    persianaCortina: "",
                    hidroneumatico: "",
                    amueblado: "",
                    piso1: "",
                    piso2: "",
                    piso3: "",
                    alarma: "",
                    urlGoogleMap: "",
                    cocinaIntegral: "",
                    vitropiso: "",
                    closet: "",
                    barda: "",
                    patioEncementado: "",
                    equipada: "",
                    pais: "",
                    estado: "",
                    municipio: "",
                    ciudad: "",
                    colonia: "",
                    codigoPostal: "",
                    calle: "",
                    numExterior: "",
                    numInterior: "",
                    entreCalle1: "",
                    entreCalle2: "",
                    nombreComplejo: "",
                    escrituracion: "",
                    avaluo: "",
                    impuestos: "",
                    otros: "",
                    total: "",
                    imagen: []
                },
                api:"http://localhost:5173/"
            };
        },
   methods:{
    createVivienda(e){
            e.preventDefault();
    },
    handleFileUpload(e) {
      this.vivienda.imagen = e.target.files;
    },
        createVivienda(){
            let json = {
                "fechaInicio": this.vivienda.fechaInicio,
                "fechaFin": this.vivienda.fechaFin,
                "empresa": this.vivienda.empresa,
                "agente": this.vivienda.agente,
                "ocultarDir": this.vivienda.ocultarDir,
                "exclusivo": this.vivienda.exclusivo,
                "titulo": this.vivienda.titulo,
                "comentario": this.vivienda.comentario,
                "tipoVivienda": this.vivienda.tipoVivienda,
                "usoActual": this.vivienda.usoActual,
                "usoPermitido": this.vivienda.usoPermitido,
                "condicionFisica": this.vivienda.condicionFisica,
                "precioVenta": this.vivienda.precioVenta,
                "precioRenta": this.vivienda.precioRenta,
                "precioMinimo": this.vivienda.precioMinimo,
                "precioPromedio": this.vivienda.precioPromedio,
                "precioMaximo": this.vivienda.precioMaximo,
                "comision1": this.vivienda.comision1,
                "ganancia1": this.vivienda.ganancia1,
                "comision2": this.vivienda.comision2,
                "ganancia2": this.vivienda.ganancia2,
                "disponibilidad": this.vivienda.disponibilidad,
                "claseInmueble": this.vivienda.claseInmueble,
                "numeroFrentes": this.vivienda.numeroFrentes,
                "medidaTerreno": this.vivienda.medidaTerreno,
                "m2Terreno": this.vivienda.m2Terreno,
                "construccionN1": this.vivienda.construccionN1,
                "construccionN2": this.vivienda.construccionN2,
                "construccionN3": this.vivienda.construccionN3,
                "gravamen": this.vivienda.gravamen,
                "valorGravamen": this.vivienda.valorGravamen,
                "valorAvaluo": this.vivienda.valorAvaluo,
                "operacion": this.vivienda.operacion,
                "condicionPago": this.vivienda.condicionPago,
                "aceptaInfonavit": this.vivienda.aceptaInfonavit,
                "aceptaFovisste": this.vivienda.aceptaFovisste,
                "propietario": this.vivienda.propietario,
                "claveCastratal": this.vivienda.claveCastratal,
                "lote": this.vivienda.lote,
                "manzana": this.vivienda.manzana,
                "cuentaAgua": this.vivienda.cuentaAgua,
                "autosEst": this.vivienda.autosEst,
                "autosIndep": this.vivienda.autosIndep,
                "estacionamiento": this.vivienda.estacionamiento,
                "cocheraElectrica": this.vivienda.cocheraElectrica,
                "patio": this.vivienda.patio,
                "asador": this.vivienda.asador,
                "fuentes": this.vivienda.fuentes,
                "jacuzzi": this.vivienda.jacuzzi,
                "alberca": this.vivienda.alberca,
                "jardin": this.vivienda.jardin,
                "bodega": this.vivienda.bodega,
                "cisterna": this.vivienda.cisterna,
                "tinaco": this.vivienda.tinaco,
                "acCentral": this.vivienda.acCentral,
                "proteccionVentana": this.vivienda.proteccionVentana,
                "persianaCortina": this.vivienda.persianaCortina,
                "hidroneumatico": this.vivienda.hidroneumatico,
                "amueblado": this.vivienda.amueblado,
                "piso1": this.vivienda.piso1,
                "piso2": this.vivienda.piso2,
                "piso3": this.vivienda.piso3,
                "alarma": this.vivienda.alarma,
                "urlGoogleMap": this.vivienda.urlGoogleMap,
                "cocinaIntegral": this.vivienda.cocinaIntegral,
                "vitropiso": this.vivienda.vitropiso,
                "closet": this.vivienda.closet,
                "barda": this.vivienda.barda,
                "patioEncementado": this.vivienda.patioEncementado,
                "equipada": this.vivienda.equipada,
                "pais": this.vivienda.pais,
                "estado": this.vivienda.estado,
                "municipio": this.vivienda.municipio,
                "ciudad": this.vivienda.ciudad,
                "colonia": this.vivienda.colonia,
                "codigoPostal": this.vivienda.codigoPostal,
                "calle": this.vivienda.calle,
                "numExterior": this.vivienda.numExterior,
                "numInterior": this.vivienda.numInterior,
                "entreCalle1": this.vivienda.entreCalle1,
                "entreCalle2": this.vivienda.entreCalle2,
                "nombreComplejo": this.vivienda.nombreComplejo,
                "escrituracion": this.vivienda.escrituracion,
                "avaluo": this.vivienda.avaluo,
                "impuestos": this.vivienda.impuestos,
                "otros": this.vivienda.otros,
                "total": this.vivienda.total,
                "imagen": this.vivienda.imagen,

            };

            axios.post(this.api+"Createvivienda", json)
            .then(data=>{console.log(data);});
        }
    }
};
</script>
<style scoped>
body {
    margin-top: 20px;
    font-family: Arial, sans-serif;
}

form {
    width: 90%;
    max-width: 600px; /* Limitamos el ancho máximo del formulario */
    margin: 0 auto;
}

section {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="number"],
textarea,
select,
input[type="date"] {
    width: calc(100% - 12px);
    padding: 8px;
    margin-top: 5px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    float: right;
}

input[type="submit"]:hover {
    background-color: #45a049;
}

.decoration-line {
  height: 40px; /* Grosor de la línea */
  width: 100%; /* Ancho completo */
  background-color: #093b59; /* Color azul */
}

</style>