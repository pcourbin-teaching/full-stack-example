/* https://dotnetthoughts.net/how-to-generate-angular-code-from-openapi-specifications/
https://github.com/swagger-api/swagger-codegen/blob/master/samples/client/petstore/typescript-angular-v4/npm/README.md
https://blog.thoughtram.io/angular/2017/11/20/custom-overlays-with-angulars-cdk.html
*/
import { Component, OnInit, ViewChild, ChangeDetectorRef } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { MatIconModule } from '@angular/material/icon';

import { ThemeService, Theme } from '../../../SPOTAPI';

import { ThemeFormPatchComponent } from '../theme-form-patch/theme-form-patch.component';
import { ThemeFormNewComponent } from '../theme-form-new/theme-form-new.component';
import { OverlayWithInjectionService, PORTAL_DATA } from '../overlay-with-injection.service';

import {Observable} from 'rxjs';

@Component({
  selector: 'app-theme-table',
  templateUrl: './theme-table.component.html',
  styleUrls: ['./theme-table.component.scss']
})
export class ThemeTableComponent implements OnInit {

  public columnsToDisplay = ['id', 'title', 'edit'];
  public themes: MatTableDataSource<Theme>;

  public themes$: Observable<Theme[]>;
  constructor(private themeService: ThemeService,
              private overlay: OverlayWithInjectionService,
              private changeDetectorRefs: ChangeDetectorRef) {
    this.refresh();
  }

  refresh(){
    this.themeService.themeGet().subscribe(data => {
      this.themes = new MatTableDataSource<Theme>(data);
      this.themes.sort = this.sort;
      this.themes.paginator = this.paginator;
      this.changeDetectorRefs.detectChanges();
    });
  }

  @ViewChild(MatSort, {static: true}) sort: MatSort;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  ngOnInit(): void { }

  delete(theme) {
    this.themeService.themesThemeIDDelete(theme.id).subscribe(result => {
      this.refresh();
    });
  }

  edit(theme) {
    this.overlay.edit(theme, ThemeFormPatchComponent);
  }

  add() {
    this.overlay.edit(null, ThemeFormNewComponent);
  }
}
