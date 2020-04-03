//PAGE D'ACCUEIL

/* eslint-disable import/first */
const API_URL = process.env.API_URL || "http://localhost:4000";
import React, { Component } from 'react';
import logo from '../logo.svg';
import '../full.css';
class Home extends Component {

  // le state correspond à des objets qui sont utilisés tout le long du code
    state = {
        debats: []
    }

    // correpond au fonction que l'on va éxecuter quand on charge la page
    componentDidMount() {
        this.getDebats();
    }

    // cette fonction récupère dans la variables debats, le json présent à l'adresse donnée en dessous
    getDebats = _ => {
        fetch(`http://localhost:4000`)
            .then(response => response.json())
            .then(response => this.setState({ debats: response.data }))
            .catch(err => console.error(err))
    }

    //cette fonction permet d'afficher en front la liste des proposition d'action
    renderDebats() {
        return this.state.debats.map(({ idcitation, cnom, texte, cnature, completude }) => {
            return (
                <tr key={idcitation}>
                    <td > {cnom}</td>
                    <a href="/citations">Acceder au débat</a>
                </tr>
            );
        });
    }

    //fonction qui affiche toute la page d'acceuil

    render() {

        return (
            <div>
                <h1>Bienvenue sur Debats_IDO </h1>
                <table id='sous_titre'>
                    <h2> Liste des debats </h2>
                </table>
                <table id='debats'>
                    <thead>
                        <tr>
                            <th scope="col">Nom</th>
                            <th scope="col">Acceder au debat</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.renderDebats()}
                    </tbody>
                </table>

            </div>
        );
    }

}

export default Home;
