import { Injectable } from '@angular/core';

import { InjectionToken, Injector } from '@angular/core';
import { ComponentPortal, PortalInjector } from '@angular/cdk/portal';
import { Overlay, OverlayRef, OverlayConfig } from '@angular/cdk/overlay';
import { Observable, of } from 'rxjs';

export const PORTAL_DATA = new InjectionToken<{}>('PortalData');

@Injectable({
  providedIn: 'root'
})
export class OverlayWithInjectionService {

  public overlayRef: OverlayRef;

  constructor(private overlay: Overlay, private injector: Injector) {
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

  edit(object, typeObject) {
    const portal = new ComponentPortal(typeObject, null, this.createInjector({object, 'overlay' : this.overlayRef}));
    const componentRef = this.overlayRef.attach(portal);
  }

  private createInjector(data): PortalInjector {
    const injectorTokens = new WeakMap<any, any>([
      [PORTAL_DATA, data],
    ]);
    return new PortalInjector(this.injector, injectorTokens);
  }
}
