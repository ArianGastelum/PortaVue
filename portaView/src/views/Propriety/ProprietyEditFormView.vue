<template>
    <div class="decoration-line"></div>
    <body>
    <form action="#" name="solucionFormulario">
    <!-- ######### Seccion de fechas ######## -->
    <section>
    <h3>Fechas</h3>      
	<label for="fechaInicio">Fecha Inicio:</label>
	<input type="date" id="fechaInicio" name="fechaInicio">

	<label for="fechaFin">Fecha Fín:</label>
	<input type="date" id="fechaFin" name="fechaFin">
    </section>
    
     <!-- ######### seccion de informacion de la propiedad ######## -->
    <section>
    <h3>Información de la propiedad:</h3>      
	<label for="titulo">Título:</label>
	<input type="text" id="titulo" name="titulo" placeholder="Escribe el título de la propiedad" maxlength="80">

	<label for="comentario">Comentario:</label>
	<textarea name="comentario" id="comentario" maxlength="800"></textarea>

    <select name="tipoVivienda" id="tipoVivienda">
      <option value="Departamento">Departamento</option>
      <option value="Vivienda">Vivienda</option>
    </select>

    <label for="usoActual">Uso Actual:</label>
	<input type="text" id="usoActual" name="usoActual" placeholder="Escribe el uso actual de la propiedad" maxlength="80">

    <label for="usoPermitido">Uso Permitido:</label>
	<input type="text" id="usoPermitido" name="usoPermitido" placeholder="Escribe el uso permitido de la propiedad" maxlength="80">

    <label for="condicionFísica">Condición Física:</label>
	<textarea name="comentario" id="comentario" maxlength="800"></textarea>

    <label for="claseInmueble">Clase de Inmueble:</label>
	<input type="text" id="claseInmueble" name="claseInmueble" placeholder="Escribe la clase de inmueble de la propiedad" maxlength="80">

    <label for="numeroFrentes">Número de Frentes:</label>
	<input type="number" id="numeroFrentes" name="numeroFrentes">

    <label for="medidaTerreno">Medida del Terreno:</label>
	<input type="text" id="medidaTerreno" name="medidaTerreno" placeholder="Escribe la medida de la propiedad" maxlength="80">

    <label for="m2Terreno">M2 del Terreno:</label>
	<input type="text" id="m2Terreno" name="m2Terreno" placeholder="Escribe los m2 de la propiedad" maxlength="80">

    <label for="construccionN1">Construccion N1:</label>
	<input type="text" id="construccionN1" name="construccionN1" placeholder="8" maxlength="80">

    <label for="construccionN2">Construccion N2:</label>
	<input type="text" id="construccionN2" name="construccionN2" placeholder="8" maxlength="80">
    
    <label for="construccionN3">Construccion N3:</label>
	<input type="text" id="construccionN3" name="construccionN3" placeholder="8" maxlength="80">

    <label for="gravamen">Gravamen:</label>
	<input type="text" id="gravamen" name="gravamen" placeholder="8" maxlength="80">
     <!-- ######### En duda ######## -->
    <label for="valorGravamen">Valor de Gravamen:</label>
	<input type="text" id="valorGravamen" name="valorGravamen" placeholder="Escribe el valor del gravamen" maxlength="80">

    <label for="valorGravamen">Valor segun Avaúo:</label>
	<input type="text" id="valorGravamen" name="valorGravamen" placeholder="Escribe el valor del gravamen" maxlength="80">

    <label for="operacion">Operación:</label>
	<input type="text" id="operacion" name="operacion" placeholder="Escribe la operacion" maxlength="80">

    <label for="condicionPago">Condición de Pago:</label>
	<input type="text" id="condicionPago" name="condicionPago" placeholder="Escribe la condición de pago" maxlength="80">

    <label for="escrituracion">Escrituración:</label>
	<input type="text" id="condicionPago" name="condicionPago" placeholder="Escribe la escrituración" maxlength="80">

    <label for="avaluo">Avalúo:</label>
	<input type="text" id="avaluo" name="avaluo" placeholder="Escribe el avalúo de la propiedad" maxlength="80">

    <label for="impuestos">Impuestos:</label>
	<input type="text" id="impuestos" name="impuestos" placeholder="Escribe el avalúo de la propiedad" maxlength="80">

    <label for="otros">Otros:</label>
	<textarea name="otros" id="otros" maxlength="400"></textarea>

    <label for="total">Total:</label>
	<input type="text" id="total" name="total" placeholder="Escribe el avalúo de la propiedad" maxlength="80">
    </section>
    
    <!-- ######### seccion de precios y comisiones ######## -->
    <section>
    <h3>Precios y comisiones</h3>
    <label for="precioVenta">Precio de  Venta:</label>
	<input type="text" id="precioVenta" name="precioVenta" placeholder="Escribe el precio de venta de la propiedad" maxlength="80">

    <label for="precioRenta">Precio de Renta:</label>
	<input type="text" id="precioRenta" name="precioRenta" placeholder="Escribe el precio de renta de la propiedad" maxlength="80">

    <label for="precioMinimo">Precio Minimo:</label>
	<input type="text" id="precioMinimo" name="precioMinimo" placeholder="Escribe el precio minimo de la propiedad" maxlength="80">

    <label for="precioPromedio">Precio Promedio:</label>
	<input type="text" id="precioPromedio" name="precioPromedio" placeholder="Escribe el precio promedio de la propiedad" maxlength="80">

    <label for="precioMaximo">Precio Maximo:</label>
	<input type="text" id="precioMaximo" name="precioMaximo" placeholder="Escribe el precio maximo de la propiedad" maxlength="80">
    
    <label for="comision1">Comision1:</label>
	<input type="text" id="comision1" name="comision1" placeholder="Escribe la comision de la propiedad" maxlength="80">

    <label for="ganancia1">Ganancia1:</label>
	<input type="text" id="ganancia1" name="ganancia1" placeholder="Escribe la ganancia de la propiedad" maxlength="80">
    
    <label for="comision2">Comision2:</label>
	<input type="text" id="comision2" name="comision2" placeholder="Escribe la comision de la propiedad" maxlength="80">

    <label for="ganancia2">Ganancia2:</label>
	<input type="text" id="ganancia2" name="ganancia2" placeholder="Escribe la ganancia de la propiedad" maxlength="80">
    </section>

    <!-- ######### seccion de la disponibilidad y exclusividad ######## -->
    <Section>
    <h3>Disponibilidad y exclusividad</h3>
    <select name="tipoDisponibilidad" id="tipoDisponibilidad">
        <option value="Disponibilidad">Disponibilidad</option>
        <option value="Exclusividad">Exclusividad</option>
    </select>    
    </Section>
    <!-- ######### seccion de la transaccion de la propiedad ######## -->
    <section>
    <h3>Información de la transacción de la propiedad</h3>
    <label for="empresa">Empresa:</label>
    <input type="text" id="empresa" name="empresa" maxlength="60">

    <label for="agente">Agente:</label>
    <input type="text" id="agente" name="agente" maxlength="50">

    <label for="propietario">Propietario:</label>
    <input type="text" id="propietario" name="propietario" maxlength="50">

    <label for="claveCastratal">Clave Catastral:</label>
    <input type="text" id="claveCastratal" name="claveCastratal" maxlength="30">

    <label for="lote">Lote:</label>
    <input type="text" id="lote" name="lote" maxlength="30">

    <label for="manzana">Manzana:</label>
    <input type="text" id="manzana" name="manzana" maxlength="30">

    <label for="cuentaAgua">Cuenta de Agua:</label>
    <input type="checkbox" id="cuentaAgua" name="cuentaAgua" maxlength="30">

    <label for="autosEst">Autos Estacionados:</label>
    <input type="number" id="autosEst" name="autosEst" min="0" max="10">

    <label for="autosIndep">Autos Independientes:</label>
    <input type="number" id="autosIndep" name="autosIndep" min="0" max="10">

    <label for="estacionamiento">Estacionamiento:</label>
    <input type="text" id="estacionamiento" name="estacionamiento" maxlength="30">

    <label for="cocheraElectrica">Cochera Eléctrica:</label>
    <input type="text" id="cocheraElectrica" name="cocheraElectrica">

    <label for="patio">Patio:</label>
    <input type="text" id="patio" name="patio" maxlength="30">

    <label for="asador">Asador:</label>
    <input type="text" id="asador" name="asador" maxlength="70">

    <label for="fuentes">Fuentes:</label>
    <input type="text" id="fuentes" name="fuentes" maxlength="90">

    <label for="jacuzzi">Jacuzzi:</label>
    <input type="text" id="jacuzzi" name="jacuzzi" maxlength="120">

    <label for="alberca">Alberca:</label>
    <input type="text" id="alberca" name="alberca" maxlength="70">

    <label for="jardin">Jardín:</label>
    <input type="text" id="jardin" name="jardin" maxlength="30">

    <label for="bodega">Bodega:</label>
    <input type="text" id="bodega" name="bodega" maxlength="50">

    <label for="cisterna">Cisterna:</label>
    <input type="text" id="cisterna" name="cisterna" maxlength="45">

    <label for="tinaco">Tinaco:</label>
    <input type="text" id="tinaco" name="tinaco" maxlength="45">

    <label for="acCentral">Aire Central:</label>
    <input type="checkbox" id="acCentral" name="acCentral">

    <label for="proteccionVentana">Protección de Ventana:</label>
    <input type="checkbox" id="proteccionVentana" name="proteccionVentana">

    <label for="persianaCortina">Persiana Cortina:</label>
    <input type="checkbox" id="persianaCortina" name="persianaCortina">

    <label for="hidroneumatico">Hidroneumático:</label>
    <input type="checkbox" id="hidroneumatico" name="hidroneumatico">

    <label for="patioEncementado">Patio Encementado:</label>
    <input type="checkbox" id="patioEncementado" name="patioEncementado" maxlength="30">

    <label for="cocina integral">Cocina integral:</label>
    <input type="text" id="cocina integral" name="cocina integral" maxlength="45">

    <label for="amueblado">Amueblado:</label>
    <input type="checkbox" id="amueblado" name="amueblado">

    <label for="piso1">Piso 1:</label>
    <input type="text" id="piso1" name="piso1" maxlength="30">

    <label for="piso2">Piso 2:</label>
    <input type="text" id="piso2" name="p1iso2" maxlength="30">

    <label for="piso3">Piso 3:</label>
    <input type="text" id="piso3" name="piso3" maxlength="30">

    <label for="alarma">URL Google Maps:</label>
    <input type="text" id="alarma" name="alarma" maxlength="30">

    <label for="vitropiso">Tipo de Vitropiso:</label>
    <input type="text" id="vitropiso" name="vitropiso" maxlength="80">

    <label for="closet">Closet:</label>
    <input type="text" id="closet" name="closet" maxlength="30">

    <label for="barda">Barda:</label>
    <input type="text" id="barda" name="barda" maxlength="30">

    <label for="equipada">Equipada:</label>
    <input type="text" id="equipada" name="equipada" maxlength="30">
    </section>
        
    <!-- ######### seccion de la ubicacion ######## -->
    <section>
    <h3>Ubicación</h3>      
    <label for="pais">País:</label>
    <input type="text" id="pais" name="pais"  maxlength="30">

    <label for="estado">Estado:</label>
    <input type="text" id="estado" name="estado"  required maxlength="30">

    <label for="municipio">Municipio:</label>
    <input type="text" id="municipio" name="municipio"  required maxlength="30">

    <label for="ciudad">Ciudad:</label>
    <input type="text" id="ciudad" name="ciudad"  required maxlength="30">

    <label for="colonia">Colonia:</label>
    <input type="text" id="colonia" name="colonia"  required maxlength="30">

    <label for="codigoPostal">Código Postal:</label>
    <input type="text" id="codigoPostal" name="codigoPostal"  required maxlength="30">

    <label for="calle">Calle:</label>
    <input type="text" id="calle" name="calle"  required maxlength="30">

    <label for="numExterior">Número Exterior:</label>
    <input type="text" id="numExterior" name="numExterior"  required maxlength="30">

    <label for="numInterior">Número Interior:</label>
    <input type="text" id="numInterior" name="numInterior"  required maxlength="30">

    <label for="entreCalle1">Entre calle 1:</label>
    <input type="text" id="entreCalle1" name="entreCalle1"  required maxlength="30">

    <label for="entreCalle2">Entre calle 2:</label>
    <input type="text" id="entreCalle2" name="entreCalle2"  required maxlength="30">

    <label for="nombreComplejo">Nombre Complejo:</label>
    <input type="text" id="nombreComplejo" name="nombreComplejo"  required maxlength="60">
    </section>

    <!-- ######### seccion de la imagen ######## -->
    <section>
    <label for="avatar">Ingrese las imagenes de la vivienda:</label>
    <input type="file" id="avatar" name="avatar" accept="image/png, image/jpeg" multiple />
    </section>

    <button type="summit" class="button-primary">Create</button>

</form>
</body>
</template>
<script>
    export default{
    }
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