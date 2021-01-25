import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProtagonistFormPatchComponent } from './protagonist-form-patch.component';

describe('ProtagonistFormPatchComponent', () => {
  let component: ProtagonistFormPatchComponent;
  let fixture: ComponentFixture<ProtagonistFormPatchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProtagonistFormPatchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProtagonistFormPatchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
