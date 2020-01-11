//Importamos las librerias ........................................................................

//importamos la conexion
import firebase from '../conexion/Conexion';

/*Esta clase hace los inserts en la lista de solicitudes para registro en la bd. */

//creamos la clase crearcount----------------------------------------------------------------------
 const insertDatosFerreteria = (ferreteria) => {
                firebase.database().ref('SolicitudesRegistro/'+ferreteria.NIT).set({
                        nombresAdmin: ferreteria.nombresAdmin,
                        apellidosAdmin: ferreteria.apellidosAdmin,
                        numerocelularAdmin: ferreteria.numerocelularAdmin,
                        numeroCCAdmin: ferreteria.numeroCCAdmin,
                        correoAdmin: ferreteria.correoAdmin,
                        nombreFerreteria: ferreteria.nombreFerreteria,
                        NIT: ferreteria.NIT,
                        telefono: ferreteria.telefono,
                        direccion: ferreteria.direccion,
                        correo: ferreteria.correo
                      });}
                      
export default insertDatosFerreteria;