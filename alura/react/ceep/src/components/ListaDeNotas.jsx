import React, { Component } from "react";
import CardNota from "./CardNota";

export class ListaDeNotas extends Component {
  render() {
    return (
      <ul>
        <li>
          <CardNota/>
        </li>
        <li>
          <CardNota/>
        </li>
        <li>
          <CardNota/>
        </li>
        <li>
          <CardNota/>
        </li>
      </ul>
    );
  }
}
