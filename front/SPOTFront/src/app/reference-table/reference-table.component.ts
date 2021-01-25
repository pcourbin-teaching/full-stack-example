import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { MatIconModule } from '@angular/material/icon';

import { ReferenceService, Reference } from '../../../SPOTAPI';
import { ReferenceSmallComponent } from '../reference-small/reference-small.component';
import { OverlayWithInjectionService, PORTAL_DATA } from '../overlay-with-injection.service';

@Component({
  selector: 'app-reference-table',
  templateUrl: './reference-table.component.html',
  styleUrls: ['./reference-table.component.scss']
})


export class ReferenceTableComponent implements OnInit {

  public columnsToDisplay = [ 'id', 'typeTitle', 'url', 'title', 'details', 'date', 'reliability', 'edit' ];
  public references: MatTableDataSource<Reference>;

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

  constructor(private referenceService: ReferenceService, private overlay: OverlayWithInjectionService) {
    referenceService.referenceGet().subscribe(data => {
      this.references = new MatTableDataSource<Reference>(data);
      this.references.sort = this.sort;
      this.references.paginator = this.paginator;
    });
  }

  @ViewChild(MatSort, {static: true}) sort: MatSort;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  ngOnInit(): void {
  }

  view(reference) {
    this.overlay.edit(reference, ReferenceSmallComponent);
  }
}
