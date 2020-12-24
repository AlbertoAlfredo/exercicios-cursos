import React, { Component } from "react";
//import { render } from "react-dom";
import { FormularioCadastro } from "./components/FormularioCadastro";
import {ListaDeNotas} from "./components/ListaDeNotas"
class App extends Component {
  render(){
    return (
      <section>
        <FormularioCadastro/>
        <ListaDeNotas/>
      </section>
    );
  }
  
}

export default App;
