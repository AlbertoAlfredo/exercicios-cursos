import React from "react";
import {ListaDeNotas} from "./components/ListaDeNotas"
function App() {
  return (
    <section>
      <form>
        <input type="Text" placeholder="Título"/>
        <textarea placeholder="Escreva sua nota"/>
        <button>Criar</button>
      </form>
      <ListaDeNotas/>
    </section>
  );
}

//react -> lib
//React -> Ecossistema
export default App;
