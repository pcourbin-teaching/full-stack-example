import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ThemeFormPatchComponent } from './theme-form-patch.component';

describe('ThemeFormPatchComponent', () => {
  let component: ThemeFormPatchComponent;
  let fixture: ComponentFixture<ThemeFormPatchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ThemeFormPatchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ThemeFormPatchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
