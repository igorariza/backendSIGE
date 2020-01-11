/*
 El archivo conexión, es el encargado de establecer
 la conexión entre la Apweb y la base datos en firebase
*/
//importamos la base de datos
import firebase from 'firebase';


//constante de configuracion:
const firebaseConfig = {
  apiKey: "AIzaSyDHRMaXkouQyVv35pldkiNYuIGmzsqEnu8",
  authDomain: "sige-474ab.firebaseapp.com",
  databaseURL: "https://sige-474ab.firebaseio.com",
  projectId: "sige-474ab",
  storageBucket: "sige-474ab.appspot.com",
  messagingSenderId: "844929643896",
  appId: "1:844929643896:web:742a706be2cfa4e3e3448d",
  measurementId: "G-4PNRX8TZPR"
  };

//constante que inicia la conexión.
const conexion = firebase.initializeApp(firebaseConfig);
 
//exporta la conexión
export default conexion;
