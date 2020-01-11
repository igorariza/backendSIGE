//Importamos las librerias ........................................................................

//importamos la conexion
import servicesRef from "../conexion/database/ServicesRef";

/*Esta clase hace las consultas para los Sercicios en la bd. */

//método para traer todos los servicios disponibles
const getServices = () => {
  //trae toda la collección de la rama servicios
  var allServices = [];
  servicesRef
    .get()
  .then(snapshot => {
   allServices = snapshot.map(doc => {
     return doc.data()
    });
  })
  .catch(err => {
    console.log('Error getting documents', err);
  });
  //regresa la lista de servicios
  console.log(allServices)
  return allServices;
};

export default getServices;
