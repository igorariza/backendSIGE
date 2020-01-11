//Importamos las librerias ........................................................................

//importamos la conexion
import conexion from '../Conexion';

//Creamos el acceso a la Colleccion Servicios
const usuariosRef = conexion.firestore().collection('USUARIOS');

//exportamos la referencia a la raiz servicios
export default usuariosRef;
