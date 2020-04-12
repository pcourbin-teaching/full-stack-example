/* https://dotnetthoughts.net/how-to-generate-angular-code-from-openapi-specifications/
https://github.com/swagger-api/swagger-codegen/blob/master/samples/client/petstore/typescript-angular-v4/npm/README.md
https://blog.thoughtram.io/angular/2017/11/20/custom-overlays-with-angulars-cdk.html
*/
import { Component, OnInit, ViewChild, InjectionToken, Injector } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';

import { ThemeService, Theme } from '../../../DebatIDOAPI';

import { Injectable } from '@angular/core';
import { ComponentPortal, PortalInjector } from '@angular/cdk/portal';
import { Overlay, OverlayRef, OverlayConfig } from '@angular/cdk/overlay';
import { ThemeFormPatchComponent } from '../theme-form-patch/theme-form-patch.component';

export const PORTAL_DATA = new InjectionToken<{}>('PortalData');

@Component({
  selector: 'app-theme-table',
  templateUrl: './theme-table.component.html',
  styleUrls: ['./theme-table.component.scss']
})
@Injectable({
  providedIn: ThemeFormPatchComponent
})
export class ThemeTableComponent implements OnInit {

  public columnsToDisplay = ['id', 'title', 'edit'];
  public themes: MatTableDataSource<Theme>;

  private overlayRef: OverlayRef;

  constructor(private themeService: ThemeService, private overlay: Overlay, private injector: Injector) {
    themeService.themeGet().subscribe(data => {
      this.themes = new MatTableDataSource<Theme>(data);
      this.themes.sort = this.sort;
      this.themes.paginator = this.paginator;
    });

    const positionStrategy = this.overlay.position()
      .global()
      .centerHorizontally()
      .centerVertically();

    const overlayConfig = new OverlayConfig({
      hasBackdrop: true,
      backdropClass: 'dark-backdrop',
      panelClass: 'tm-file-preview-dialog-panel',
      scrollStrategy: this.overlay.scrollStrategies.block(),
      positionStrategy
    });

    this.overlayRef = this.overlay.create(overlayConfig);

    this.overlayRef.backdropClick().subscribe(() => {
      this.overlayRef.detach();
    });
  }

  @ViewChild(MatSort, {static: true}) sort: MatSort;
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  ngOnInit(): void {

  }

  edit(theme) {
    const portal = new ComponentPortal(ThemeFormPatchComponent, null, this.createInjector({theme, 'overlay' : this.overlayRef}));
    const componentRef = this.overlayRef.attach(portal);
  }

  private createInjector(data): PortalInjector {
    const injectorTokens = new WeakMap<any, any>([
      [PORTAL_DATA, data],
    ]);
    return new PortalInjector(this.injector, injectorTokens);
  }
}
