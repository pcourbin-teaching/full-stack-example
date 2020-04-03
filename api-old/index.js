/* Dans ce fichier, nous nous connectons à la base de données MySQL pour récupérer
les différentes données dont nous avons besoin */

/* Ces premièr ligne permette de ce connecter à mysql en entrer le host de mysql,
le nom du user, le mot de passe et le nom de la base de données */
/* Ces variables peuvent être récupérées directement dans l'envrionnement défini
par l'utilisateur ou sont données directement */
const PORT = process.env.PORT || 3000;
const DB_HOST = process.env.DB_HOST || "localhost"; // par exemple ici, le programme récupère soit le host défini dans l'envrionnement, soit le localhost
const DB_USER = process.env.DB_USER || "root";
const DB_PASSWORD = process.env.DB_PASSWORD || "TishTish1998";
const DB_NAME = process.env.DB_NAME || "debatsido";

// importation de différentes library qui serviront dans la suite du programme
const express = require('express');
const cors = require('cors');
const app = express();
const mysql = require('mysql');
app.use(cors());

// ici nous déclarons les premières requêtes sql
const selectAll = 'Select * from citation';

// nous délarons la connection faite avec mysql
const connection = mysql.createConnection({
    host: DB_HOST,
    user: DB_USER,
    password: DB_PASSWORD,
    database: DB_NAME
});
//nous nous connectons à la base de données
connection.connect(err => { if (err) { return err; } });


// Fonction qui applicque la query selectAll, query qui récupère tous les instances de la table citation
// le /citation indique l'adresse à laquelle se trouve le résultat JSON de la query
app.get('/citation', (req, res) => {
    connection.query(selectAll, (err, results) => {
        if (err) { return res.send(err) } else {
            return res.json({ data: results }) //le résultat est retrouné en format json grâce à res.json
        }
    });
});

// Fonction qui récupère une citation selon un id donné en argument (servira par la suite à afficher une citation mère)
app.get('/citation/mere',(req,res) => {
  const { idcitation_mere } = req.query;
  const querycitmere = `SELECT * from citation where idcitation=${idcitation_mere}`;
  connection.query(querycitmere,(err,results)=>{
    if(err){return res.send(err)}
    else {
      return res.json({data:results})
    }
  })
})

// Fonction qui récupère les citations filles d'une citation mère dont l'id est donné en argument
app.get('/citation/filles',(req,res) => {
  const { idcitation_mere } = req.query;
  const querycitfilles = `SELECT c2.*,lien_citation.positionnement from citation c1, citation c2, lien_citation where c1.idcitation=id_cit1 and c2.idcitation=id_cit2 and c1.idcitation=${idcitation_mere}`;
  connection.query(querycitfilles,(err,results)=>{
    if(err){return res.send(err)}
    else {
      return res.json({data:results})
    }
  });
})

//Fonction qui récupère l'id citation mère d'une citation fille dont l'id est donné en argument
app.get('/citation/back',(req,res) =>{
  const {idcitation_mere}= req.query;
  const querycitback = `SELECT id_cit1 from lien_citation where id_cit2=${idcitation_mere}`
  connection.query(querycitback,(err,results)=>{
    if(err){return res.send(err)}
    else {
      return res.json({data:results})
    }
  });
})

//Fonction qui permet d'ajouter à la table lien_citation l'id de la citation que l'on vient d'ajouter à la table citation, l'id de sa citation mère et le positionnement
function lien_citation(req) {
    const { idcitation, cnom, texte, cnature, completude, positionnement,idcitation_mere } = req.query;
    console.log(typeof idcitation)
    const Insert = `INSERT INTO lien_citation (positionnement, id_cit1, id_cit2) VALUES ('${positionnement}','${idcitation_mere}','${idcitation}')`;
    connection.query(Insert, (err, results) => {
        if (err) { throw err }
        else {
          console.log('successfully added')
        }
    });
};

// Fonction qui ajoute à la table citation, une citations dont chaque attribut est donné en argument
app.get('/citation/add', (req, res) => {
    const { idcitation, cnom, texte, cnature, completude, positionnement,idcitation_mere } = req.query;
    const Insert = `insert into citation (idcitation, cnom, texte, cnature, completude) values('${idcitation}',' ${cnom}', '${texte}',' ${cnature}', '${completude}')`;
    connection.query(Insert, (err, results) => {
        if (err) { throw err }
        else {
          console.log(results)
          req.query.idcitation=results.insertId
          lien_citation(req);
          return res.json({ data: results })
        }
    });
});

//Fonction qui permet de supprimer une citation de la table citation à partir d'un id donné en argument
app.get('/citation/delete', (req, res) => {
    const { idcitation } = req.query;
    const querysource = `DELETE FROM citation WHERE idcitation=${idcitation}`;
    connection.query(querysource, (err, results) => {
        if (err) { return res.send(err) } else {
            return res.json({ data: results })
        }
    });
})


//Fonction qui permet de récupérer les sources d'une citation dont l'id est donné en argument
app.get('/citation/source', (req, res) => {
    const { idcitation } = req.query;
    const querysource = `SELECT idmedium,date, mnature, lien, mnom,fiabilite,mtitre FROM medium JOIN lien_citation_medium ON idmedium=lien_citation_medium.idmedium_fk JOIN citation ON lien_citation_medium.idcitation_fk=idcitation WHERE idcitation=${idcitation}`;
    connection.query(querysource, (err, results) => {
        if (err) { return res.send(err) } else {
            return res.json({ data: results })
        }
    });
})


//app.listen(4000, () => { console.log('essaie') })
app.listen(PORT, () => { console.log('Lancement de l\'API sur le port '+PORT) })

const selectdebat = 'Select * from citation where cnature="proposition d action"';

//Fonction qui récupère toutes les propositions d'action pour la page d'accueil
app.get('/', (req, res) => {
    connection.query(selectdebat, (err, results) => {
        if (err) { return res.send(err) } else {
            return res.json({ data: results })
        }
    });
});

//console.log(connection);
/*app.get('/', (req, res) => {
    return res.send('Bonjour')
});*/
