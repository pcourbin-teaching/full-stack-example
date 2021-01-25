import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { MatIconModule } from '@angular/material/icon';

import { ProtagonistService, Protagonist } from '../../../SPOTAPI';

import { ProtagonistFormPatchComponent } from '../protagonist-form-patch/protagonist-form-patch.component';
import { ProtagonistFormNewComponent } from '../protagonist-form-new/protagonist-form-new.component';
import { OverlayWithInjectionService, PORTAL_DATA } from '../overlay-with-injection.service';

@Component({
  selector: 'app-protagonist-table',
  templateUrl: './protagonist-table.component.html',
  styleUrls: ['./protagonist-table.component.scss']
})
export class ProtagonistTableComponent implements OnInit {

  public columnsToDisplay = [ 'type', 'id', 'photo', 'name',  'link', 'edit' ];
  public protagonists: MatTableDataSource<Protagonist>;

  constructor(private protagonistService: ProtagonistService, private overlay: OverlayWithInjectionService) {
    this.refresh();
  }

  refresh(){
    this.protagonistService.protagonistGet().subscribe(data => {
      this.protagonists = new MatTableDataSource<Protagonist>(data);
      this.protagonists.sort = this.sort;
      this.protagonists.paginator = this.paginator;
    });
  }

  @ViewChild(MatSort, {static: true}) sort: MatSort;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  ngOnInit(): void { }

  delete(protagonist) {
    this.protagonistService.protagonistsProtagonistIDDelete(protagonist.id).subscribe(result => {
      this.refresh();
    });
  }

  edit(protagonist) {
    this.overlay.edit(protagonist, ProtagonistFormPatchComponent);
  }

  add() {
    this.overlay.edit(null, ProtagonistFormNewComponent);
  }
}
