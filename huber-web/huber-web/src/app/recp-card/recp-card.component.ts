import { Component, OnInit } from '@angular/core';
import { MatToolbar, MatCardModule } from '@angular/material'; 

@Component({
  selector: 'recp-card',
  templateUrl: './recp-card.component.html',
  styleUrls: ['./recp-card.component.css']
})
export class RecpCardComponent implements OnInit {
  name: string;
  calorie: number;
  ingredients: string;

  constructor(nameI: string, numberI: number, ingredientsI: string) {
    this.name = nameI;
    this.calorie = numberI;
    this.ingredients = ingredientsI;
  }

  ngOnInit() {

  }



}
