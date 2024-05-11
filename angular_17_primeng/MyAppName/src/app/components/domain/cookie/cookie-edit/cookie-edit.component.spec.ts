import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CookieEditComponent } from './cookie-edit.component';

describe('CookieEditComponent', () => {
  let component: CookieEditComponent;
  let fixture: ComponentFixture<CookieEditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CookieEditComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CookieEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
