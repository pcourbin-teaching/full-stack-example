import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReferenceSmallComponent } from './reference-small.component';

describe('ReferenceSmallComponent', () => {
  let component: ReferenceSmallComponent;
  let fixture: ComponentFixture<ReferenceSmallComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReferenceSmallComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReferenceSmallComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
