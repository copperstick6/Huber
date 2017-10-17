import { Component, OnInit } from '@angular/core';
import { MatToolbar, MatCardModule } from '@angular/material'; 

@Component({
  selector: 'recp-card',
  templateUrl: './recp-card.component.html',
  styleUrls: ['./recp-card.component.css']
})
export class RecpCardComponent implements OnInit {
  label: string;
  ingredientLines: string [];
  healthLabels: string [];
  dietLabels: string[];
  url: string;
  image: string;
  calories: number;

  constructor( label: string, ingredientLines: string [], healthLabels: string [], dietLabels: string[], url: string, image: string, calories: number) {
    this.label = label;
    this.ingredientLines = ingredientLines;
    this.healthLabels = healthLabels;
    this.dietLabels = dietLabels;
    this.url = url;
    this.image = image;
    this.calories = calories;
  }

  ngOnInit() {

  }



}
