import { Component, OnInit, Input, Inject, Optional } from '@angular/core';

import { ReferenceService, Reference } from '../../../SPOTAPI';

import { PORTAL_DATA } from '../overlay-with-injection.service';

@Component({
  selector: 'app-reference-small',
  templateUrl: './reference-small.component.html',
  styleUrls: ['./reference-small.component.scss']
})
export class ReferenceSmallComponent implements OnInit {

  @Input()
  public referenceID;
  @Input()
  public reference: Reference;

  /*  '1', 'Livre'
  '2', 'Précis'
  '3', 'Article Internet'
  '4', 'Article'
  '5', 'Essai'
  '6', 'Étude'
  '7', 'Interview'
  '8', 'Vidéo'
  '9', 'Revue'
  */

  public iconsType = {
    1: {
      "icon" : "book",
      "color" : "gree"
    },
    2: {
      "icon" : "book",
      "color" : "orange"
    },
    3 : {
      "icon" : "web",
      "color" : "black"
    },
    4 : {
      "icon" : "assignment",
      "color" : "green"
    },
    7 : {
      "icon" : "mic",
      "color" : "green"
    },
    8 : {
      "icon" : "video_library",
      "color" : "green"
    },
    "default" : {
      "icon" : "done_all",
      "color" : "green"
    }
  };

  constructor(@Optional() @Inject(PORTAL_DATA) public overlay, private referenceService: ReferenceService) { 
  }

  ngOnInit(): void {
    if (this.referenceID != undefined){
      this.refresh();
    }

    if (this.overlay){
      this.reference = this.overlay.object;
      this.updatePhoto();
    }
  }

  refresh(){
    this.referenceService.referencesReferenceIDGet(this.referenceID).subscribe(data => {
      this.reference = data;
      this.updatePhoto();
    });
  }

  updatePhoto() {
    for (let author of this.reference.authors) {
      if (author.photo == undefined) {
        author.photo = "assets/img/person.jpg";
      }
    }
  }

}
