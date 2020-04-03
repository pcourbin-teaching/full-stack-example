import React from 'react';
import Tree from 'react-d3-tree';
import './Citations.css';


const Cannabis = [
  {
    name: 'Il faut dépénaliser le cannabis',
    nodeSvgShape: {
      shape: 'circle',
      shapeProps: {
        r: 10,
        fill: 'blue',
      },
    },
    children: [
      {
        name: 'La prohibition est préjudiciable aux usagers',
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'green',
          },
        },
        children: [
          {
            name: 'Entrave à la prévention et aux soins',
            nodeSvgShape: {
              shape: 'circle',
              shapeProps: {
                r: 10,
                fill: 'green',
              },
            },
          },
          {
            name: 'Conséquences de séjours en prison',
            nodeSvgShape: {
              shape: 'circle',
              shapeProps: {
                r: 10,
                fill: 'green',
              },
            },
          }
        ]
      },
      {
        name: 'La prohibition est préjudiciable à la société',
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'green',
          },
          },
          children: [
            {
              name: 'Génère beaucoup de controles',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'green',
                },
              },
            },
            {
              name: 'La prohibition accroit la rentabilité',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'green',
                },
              },
            }
          ]
      },
      {
        name: "Il faut protéger l'individu",
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'red',
          },
          },
          children: [
            {
              name: 'Son pouvoir addictif est important',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            },
            {
              name: 'il est dangereux pour la santé',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            }
          ]
      },
      {
        name: "La société doit se protéger",
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'red',
          },
          },
          children: [
            {
              name: 'Il engendre des couts pour la société',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            },
            {
              name: 'Il est impliqué dans les accidents de la route',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            }
          ]
      },
    ],
  },
];

const Revenu = [
  {
    name: 'Il faut instaurer un revenu de base',
    nodeSvgShape: {
      shape: 'circle',
      shapeProps: {
        r: 10,
        fill: 'blue',
      },
    },
    children: [
      {
        name: 'Meilleurs conditions de vie',
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'green',
          },
        },
        children: [
          {
            name: 'Réduction de la pauvreté',
            nodeSvgShape: {
              shape: 'circle',
              shapeProps: {
                r: 10,
                fill: 'green',
              },
            },
          },
          {
            name: 'Dégradation des conditions de travail',
            nodeSvgShape: {
              shape: 'circle',
              shapeProps: {
                r: 10,
                fill: 'red',
              },
            },
          }
        ]
      },
      {
        name: "Bon pour l'économie du pays",
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'green',
          },
          },
          children: [
            {
              name: "Incitation à la création d'entreprises",
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'green',
                },
              },
            },
            {
              name: "Risque d'inflation",
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            }
          ]
      },
      {
        name: "Un désastre économique ",
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'red',
          },
          },
          children: [
            {
              name: "Plus personne n'ira travailler",
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            },
            {
              name: 'Baisse de compétitivité',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            }
          ]
      },
      {
        name: "Un mauvais combat politique",
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'red',
          },
          },
          children: [
            {
              name: 'Revendication trop imprécise',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            },
            {
              name: 'Abandon de la lutte pour une meilleure protection sociale',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            }
          ]
      },
    ],
  },
];

const Vote = [
  {
    name: 'Il faut généraliser le vote électronique',
    nodeSvgShape: {
      shape: 'circle',
      shapeProps: {
        r: 10,
        fill: 'blue',
      },
    },
    children: [
      {
        name: 'Favorise la participation aux elections',
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'green',
          },
        },
        children: [
          {
            name: 'Mesure incitative pour les jeunes',
            nodeSvgShape: {
              shape: 'circle',
              shapeProps: {
                r: 10,
                fill: 'green',
              },
            },
          },
          {
            name: "Difficultés pour ceux peu à l'aise avec la technologie",
            nodeSvgShape: {
              shape: 'circle',
              shapeProps: {
                r: 10,
                fill: 'red',
              },
            },
          }
        ]
      },
      {
        name: "Diminue l'empreinte écologique du vote",
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'green',
          },
          },
          children: [
            {
              name: "Moins de papier et d'urnes",
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'green',
                },
              },
            },
            {
              name: "Moins de transport pour aller voter",
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'green',
                },
              },
            }
          ]
      },
      {
        name: "Il n'est pas fiable",
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'red',
          },
          },
          children: [
            {
              name: "les ordinateurs personnels ne sont pas bien sécurisés",
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            },
            {
              name: "difficile de vérifier l'identité des votants",
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            }
          ]
      },
      {
        name: "Il est invérifiable et opaque",
        _collapsed: true,
        nodeSvgShape: {
          shape: 'circle',
          shapeProps: {
            r: 10,
            fill: 'red',
          },
          },
          children: [
            {
              name: 'Impossible de recompter les votes',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            },
            {
              name: 'les machines à voter peuvent avoir un code source libre et ouvert',
              nodeSvgShape: {
                shape: 'circle',
                shapeProps: {
                  r: 10,
                  fill: 'red',
                },
              },
            }
          ]
      },
    ],
  },
];


class Arbre extends React.Component {
  state = {
      my_index: null
  }


renderDebats() {
const debats = ['Cannabis', 'Revenu', 'Vote'];
const prop = ['Il faut dépénaliser le cannabis.', 'Il faut instaurer un reveu de base.', 'Il faut généraliser le vote électronique.'];
return debats.map((value, index) => {
      return (
        <tr key={index}>
          <td>
            <button onClick={() => {this.setState({my_index: index}); this.renderTree();}}> {value}</button>
            - {prop[index]}
          </td>
        </tr>
    );
  });
}

renderTree(){
  const smth = [Cannabis, Revenu, Vote];
  console.log("in render tree");
  if (this.state.my_index == null){
    return(
      <p style={{'whiteSpace': 'pre-wrap'}}>
        {"                        Choissisez un débat pour le visualiser \n"}
      </p>
    );
  }
  else{
    console.log("goes here");
    return <Tree data= {smth[this.state.my_index]}/>;
  }
}


render(){
  console.log("in render");
  return(
  <div>
    <p style={{'whiteSpace': 'pre-wrap'}}>
    <h1>
      {"\n \n \n     Liste des Débats: \n"}
    </h1>
    </p>
      <table id='citations'>
        <tbody>
          {this.renderDebats()}
        </tbody>
      </table>
      <div id="treeWrapper" style={{width: '50em', height: '50em'}}>
      <p style={{'whiteSpace': 'pre-wrap'}}>
      <h1>
        {"\n     Arbre des arguments: \n"}
      </h1>
      </p>
      {this.renderTree()}
      </div>
    </div>
  );
  }
}

export default Arbre;
