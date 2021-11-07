<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hoja de vida</title>
    <!--Cargar Estilos CCS-->
    <link rel="stylesheet" href="style.css" />
    <!--Cargar fuentes desde google fonts-->
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"
      rel="stylesheet"
    />
    <!--Cargar font awesome iconos -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
      integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
  </head>
  <body>
    <!--CONTENEDOR PRINCIPAL -->
    <div class="container">
      <!--LATERAL IZQUIERDO-->
      <div class="left_Side">
        <div class="profileText">
          <div class="imgBx">
            <img src="img/3x4cm.jpg" alt="Foto Perfil" />
          </div>
          <h2>
            julián Camilo Morales Agudelo<br />
            <span>Desarrollador de software</span>
          </h2>
        </div>
        <div class="contactInfo">
          <h3 class="title">Contacto</h3>

          <table class="tabla" style="color: #ffffff">
            <tr>
              <td>
                <span class="icon"
                  ><i class="fa fa-phone" aria-hidden="true"></i
                ></span>
              </td>
              <td><span class="text">(+57) 3042448822</span></td>
            </tr>

            <tr>
              <td>
                <span class="icon"
                  ><i class="fa fa-envelope" aria-hidden="true"></i
                ></span>
              </td>

              <td>
                <a href="mailto:juliancmorales10@gmail.com"  target="_blank" style="color:#ffffff" >
                  <span>juliancmorales10@gmail.com</span></a
                >
              </td>
            </tr>
            <tr>
              <td>
                <span class="icon"
                  ><i class="fa fa-globe" aria-hidden="true"></i
                ></span>
              </td>

              <td>
                <a
                  href="https://www.facebook.com/julian.morales.agudelo"
                  target="_blank"
                >
                  <span>julian.morales.fb</span></a
                >
              </td>
            </tr>

            <tr>
              <td>
                <span class="icon"
                  ><i class="fa fa-globe" aria-hidden="true"></i
                ></span>
              </td>
              <td>
                <a
                  href="https://www.linkedin.com/in/juliancmorales"
                  target="_blank"
                  ><span>juliancmorales.linkedin</span></a
                >
              </td>
            </tr>
          </table>
        </div>
        <div class="contactInfo education">
          <h3 class="title">Educación</h3>
          <ul>
            <li>
              <h5>2019 - ACTUALMENTE</h5>
              <h4>Tecnología en Desarrollo de Software</h4>
              <h4>IU Digital de Antioquia</h4>
            </li>
            <li>
              <h5>2006 - 2010</h5>
              <h4>Tecnología en Electrónica</h4>
              <h4>Institución Universitaria ITM</h4>
            </li>
            <li>
              <h5>1995 - 2001</h5>
              <h4>Bachiller Académico</h4>
              <h4>Liceo Nocturno Francisco Antonio Zea.</h4>
            </li>
          </ul>
        </div>
      </div>
      <!--LATERAL DERECHO-->
      <div class="right_Side">
        <div class="about">
          <h2 class="title2">Perfil</h2>
          <p>
            Tecnólogo en electrónica con cinco años de experiencia en el cargo
            de soporte técnico, administración e instalación de sistemas
            operativos Windows y GNU-Linux, sistemas gestores de bases de datos,
            conocimientos básicos en programación, redes, ofimática, orientación
            al aprendizaje continuo, compromiso, proactividad y dinamismo.
          </p>
        </div>
        <div class="about">
          <h2 class="title2">Experiencia</h2>
          <div class="box">
            <div class="year_company">
              <h5>ACTUALMENTE</h5>
              <h5>Emergia Customer Care</h5>
            </div>
            <div class="text">
              <h4>Tecnico de conduccion y reporting</h4>
              <ul>
                <li>Controlar la operacion, analitica de datos y reportes.</li>
              </ul>
            </div>
          </div>

          <div class="box">
            <div class="year_company">
              <h5>2015 - 2020</h5>
              <h5>Intelligent Electronic Solutions</h5>
            </div>
            <div class="text">
              <h4>Técnico de soporte</h4>
              <ul>
                <li>
                  Actualización e instalación de sistemas operativos y software
                  en general.
                </li>
                <li>
                  Administración y soporte remoto de servidores Windows -
                  Gnu_Linux y sistemas informáticos.
                </li>
                <li>Actualización base de datos.</li>
                <li>Soporte de Segundo Nivel.</li>
              </ul>
            </div>
          </div>
          <div class="box">
            <div class="year_company">
              <h5>2013 - 2014</h5>
              <h5>Red-Origen & Tecniya</h5>
            </div>
            <div class="text">
              <h4>Técnico electrónico</h4>
              <ul>
                <li>
                  Instalación de tarjetas electronicas de electrodomesticos.
                </li>
                <li>
                  Reparación de tarjetas electronicas de electrodomesticos.
                </li>
                <li>Asistencia y mantenimiento de electrodomesticos.</li>
                <li>Soporte en sitio para equipos electrodomesticos.</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="about skills">
          <h2 class="title2">Habilidades</h2>
          <div class="box">
            <h4>Java</h4>
            <div class="percent">
              <div style="width: 40%"></div>
            </div>
          </div>
          <div class="box">
            <h4>Excel</h4>
            <div class="percent">
              <div class="progress-bar" style="width: 40%"></div>
            </div>
          </div>
          <div class="box">
            <h4>Python</h4>
            <div class="percent">
              <div style="width: 40%"></div>
            </div>
          </div>
          <div class="box">
            <h4>SpringBoot</h4>
            <div class="percent">
              <div style="width: 30%"></div>
            </div>
          </div>
          <div class="box">
            <h4>SQL</h4>
            <div class="percent">
              <div style="width: 30%"></div>
            </div>
          </div>
          <div class="box">
            <h4>HTML & CSS</h4>
            <div class="percent">
              <div class="progress-bar" style="width: 20%"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <a
      href="https://api.whatsapp.com/send?phone=+573042448822"
      class="btn-wsp"
      target="_blank"
    >
      <i class="fa fa-whatsapp" aria-hidden="true"></i>
    </a>
  </body>
</html>
