// MENU EN HAUT DE LA PAGE
// Il permet d'accéder à chaque page du site selon un chemin d'acces

import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Home from './components/Home';
import Citations from './components/Citations';
import Arbre from './components/Arbre';
import Contact from './components/Contact';
import Error from './components/Error';
import Navigation from './components/Navigation';

class App extends Component {
  render() {
    return (
       <BrowserRouter>
        <div>
          <Navigation />
            <Switch>
             <Route path="/" component={Home} exact/>
             <Route path="/citations" component={Citations}/>
             <Route path="/arbre" component={Arbre}/>
             <Route path="/contact" component={Contact}/>
            <Route component={Error}/>
           </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
