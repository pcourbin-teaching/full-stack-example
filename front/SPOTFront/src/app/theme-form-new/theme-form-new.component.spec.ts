import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ThemeFormNewComponent } from './theme-form-new.component';

describe('ThemeFormNewComponent', () => {
  let component: ThemeFormNewComponent;
  let fixture: ComponentFixture<ThemeFormNewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ThemeFormNewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ThemeFormNewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
