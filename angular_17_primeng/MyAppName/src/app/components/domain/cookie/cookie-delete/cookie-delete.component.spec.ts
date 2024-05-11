import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CookieDeleteComponent } from './cookie-delete.component';

describe('CookieDeleteComponent', () => {
  let component: CookieDeleteComponent;
  let fixture: ComponentFixture<CookieDeleteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CookieDeleteComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CookieDeleteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
