// PAGE QUI AFFICHES TOUTES LES CITATIONS

import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Citations.css';

class Citations extends Component {
    state = {
        citations: [],
        citation_mere:[],
        sources: [],
        idcitation_mere:1,
        back :-1,
        citation: {
            idcitation: 0,
            cnom: 'citation name',
            texte: 'texte',
            cnature: 'cnature',
            completude:0,
            positionnement: 'pour ou contre',
            idcitationm:0
        }
    }

    // on commence par executer les fonctions qui donnent la 1ere citation mere et ses filles
    componentDidMount() {
        this.getCitationMere(this.state.idcitation_mere);
        this.getCitationsFilles(this.state.idcitation_mere);
    }

    //récupération de la citation mère
    getCitationMere(idcitation_mere){
      fetch(`http://localhost:4000/citation/mere?idcitation_mere=${idcitation_mere}`)
        .then(response => response.json())
        .then(response => this.setState({citation_mere:response.data}))
        .catch(err => console.error(err))
    }

    // récupère les citations filles d'une citation mère
    getCitationsFilles(idcitation_mere){
      fetch(`http://localhost:4000/citation/filles?idcitation_mere=${idcitation_mere}`)
        .then(response => response.json())
        .then(response => this.setState({citations:response.data}))
        .catch(err => console.error(err))
    }

    // récupération d'une citation mère de ses citations filles mais aussi de la citation mère de la citation mère (pour permettre un back)
    getArbre(event,idcitation_mere){
      event.preventDefault();
      fetch(`http://localhost:4000/citation/back?idcitation_mere=${idcitation_mere}`)
        .then(response => response.json())
        .then(response => this.setState({back:response.data[0].id_cit1}))
        .catch(err => console.error(err))
      fetch(`http://localhost:4000/citation/mere?idcitation_mere=${idcitation_mere}`)
        .then(response => response.json())
        .then(response => this.setState({
            citation_mere:response.data
        }))
          .catch(err => console.error(err))
      fetch(`http://localhost:4000/citation/filles?idcitation_mere=${idcitation_mere}`)
        .then(response => response.json())
        .then(response => this.setState({
          citations:response.data,
          idcitation_mere:idcitation_mere,
          sources:[]}))
        .catch(err => console.error(err))
    }

    //obtention de la citation mère de la citation mère actuelle et de ses citations filles
    getBack_Arbre(event) {
        event.preventDefault();
        fetch(`http://localhost:4000/citation/mere?idcitation_mere=${this.state.back}`)
        .then(response => response.json())
        .then(response => this.setState({
            citation_mere:response.data
        }))
          .catch(err => console.error(err))
      fetch(`http://localhost:4000/citation/filles?idcitation_mere=${this.state.back}`)
        .then(response => response.json())
        .then(response => this.setState({
          citations:response.data,
          idcitation_mere:this.state.back,
          sources:[]}))
        .catch(err => console.error(err))
      fetch(`http://localhost:4000/citation/back?idcitation_mere=${this.state.back}`)
        .then(response => response.json())
        .then(response => {
            if (response.data.length==0)
            {
                this.setState({back:-1});
            }
            else{
                this.setState({back:response.data[0].id_cit1});
            }
        })
        .catch(err => console.error(err))
    }

    //obtention des sources d'une citation donnée
    getSource(event, idcit) {
        event.preventDefault();
        fetch(`http://localhost:4000/citation/source?idcitation=${idcit}`)
            .then(response => response.json())
            .then(response => this.setState({ sources: response.data }))
            .catch(err => console.error(err))
    }

    //ajout d'une citation
    addCitation(event){
        const { citation } = this.state;
        fetch(`http://localhost:4000/citation/add?idcitation=${citation.idcitation}&cnom=${citation.cnom}&texte=${citation.texte}&cnature=${citation.cnature}&completude=${citation.completude}&positionnement=${citation.positionnement}&idcitation_mere=${citation.idcitationm}`)
            .then(this.getArbre(event,this.state.idcitation_mere))
            .then(this.setState({citation:{idcitation: 0,cnom: 'citation name',texte: 'texte',cnature: 'cnature',completude:0,positionnement: 'pour ou contre',idcitationm:0}}))
            .catch(err=>console.error(err))
    }

    //suppression d'une citationn
    deletecitation(e, idcit) {
        fetch(`http://localhost:4000/citation/delete?idcitation=${idcit}`)
            .then(this.getArbre(e,this.state.idcitation_mere))
            .catch(err => console.error(err))
    }

    //gestion de l'affichage des citatios
    renderCitations() {
        return this.state.citations.map(({ idcitation, cnom, texte, cnature, completude,positionnement }) => {
            return (
                <tr key={idcitation}>
                    <td > {idcitation}</td>
                    <td > {cnom}</td>
                    <td> {texte}</td>
                    <td> {cnature}</td>
                    <td> {completude} </td>
                    <td> {positionnement} </td>
                    <td><button onClick={(event) => this.getSource(event, idcitation)}> Sources </button></td>
                    <td><button onClick={(event) => this.getArbre(event, idcitation)}> {cnom} </button></td>
                    <td><button onClick={(event) => this.deletecitation(event, idcitation)}> Delete </button></td>
                </tr>
            );
        });
    }

    //gestion de l'affichage de la citation mère
    renderMere() {
        return this.state.citation_mere.map(({ idcitation, cnom, texte, cnature, completude }) => {
            return (
                <tr key={idcitation}>
                    <td> {idcitation}</td>
                    <td > {cnom}</td>
                    <td> {texte}</td>
                    <td> {cnature}</td>
                    <td> {completude} </td>
                    <button onClick={(event) => this.getSource(event, idcitation)}> Sources </button>
                </tr>
            );
        });
    }

    //gestion de l'affichage des sources
    renderSource() {
        return this.state.sources.map(({ idmedium, date, mnature, lien, mnom, fiabilite, mtitre }) => {
            return (
                <tr key={idmedium}>
                    <td>{date}</td>
                    <td>{mnature}</td>
                    <td>{lien}</td>
                    <td> {mnom} </td>
                    <td> {fiabilite} </td>
                    <td> {mtitre} </td>
                </tr>
            );
        });
    }

    //affichage total de la page
    render() {
        const citation= this.state.citation;
        return (
            <div className="Citations">
                { this.state.back!=-1 &&
                    <button id="back" onClick={(event) => this.getBack_Arbre(event)}> Back </button>
                }
                <h2> Citation </h2>
                <table id='citations'>
                    <thead>
                        <tr>
                            <th scope="col">ID</th>
                            <th scope="col">Nom</th>
                            <th scope="col">Texte</th>
                            <th scope="col">Nature</th>
                            <th scope="col">Completude</th>
                            <th scope="col">Sources</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.renderMere()}
                    </tbody>
                </table>
                <h2> Liste des arguments pour ou contre </h2>
                <table id='citations'>
                    <thead>
                        <tr>
                            <th scope="col">ID</th>
                            <th scope="col">Nom</th>
                            <th scope="col">Texte</th>
                            <th scope="col">Nature</th>
                            <th scope="col">Completude</th>
                            <th scope="col">Positionnement</th>
                            <th scope="col">Sources</th>
                            <th scope="col">Citations filles</th>
                            <th scope="col">Delete</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.renderCitations()}
                    </tbody>
                </table>
                <div>
                {this.state.sources.length!=0 && <h2> Liste des sources </h2>}
                    {this.state.sources.length!=0 &&
                    <table id='sources'>
                        <thead>
                            <tr>
                                <th scope="col">Date</th>
                                <th scope="col">Nature</th>
                                <th scope="col">Lien</th>
                                <th scope="col">Nom du media</th>
                                <th scope="col">Fiabilite</th>
                                <th scope="col">Titre</th>
                            </tr>
                        </thead>
                        <tbody>
                            {this.renderSource()}
                        </tbody>
                    </table>
                    }
                </div>
                <div>
                  <h2> Ajouter une citation </h2>
                    <label for="nomcit">Nom de la citation</label>
                    <input id="nomcit" value={citation.cnom} onChange={e => this.setState({
                        citation: { ...citation, cnom: e.target.value }
                    })} />
                    <label for="textecit">Texte de la citation</label>
                    <input id="textcit" value={citation.texte} onChange={e => this.setState({
                        citation: { ...citation, texte: e.target.value }
                    })} />
                    <label for="natcit">Nature de la citation</label>
                    <input id="natcit" value={citation.cnature} onChange={e => this.setState({
                        citation: { ...citation, cnature: e.target.value }
                    })} />
                    <label for="completude">Completude de la citation</label>
                    <input id="completude" value={citation.completude} onChange={e => this.setState({
                        citation: { ...citation, completude: e.target.value }
                    })} />
                    <label for="pos">Positionnement de la citation par rapport à sa citation mère</label>
                    <input id="pos" value={citation.positionnement} onChange={e => this.setState({
                        citation: { ...citation, positionnement: e.target.value }
                    })} />
                    <label for="mere">ID de la citation mere</label>
                    <input id="mere" value={citation.idcitationm} onChange={e => this.setState({
                        citation: { ...citation, idcitationm: e.target.value }
                    })} />
                    <button id="add" onClick={(event) => this.addCitation(event)}>Add</button>
                </div>
            </div>
        );
    }
}

export default Citations;
