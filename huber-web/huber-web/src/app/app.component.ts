import { Component, OnInit } from '@angular/core';
import { MatToolbar, MatGridList, MatGridTile } from '@angular/material'; 
import { RecpCardComponent } from './recp-card/recp-card.component';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  // cards : RecpCardComponent[];

  constructor(private http: HttpClient){
  
  }
  
  ngOnInit(): void {
    this.http.get('http://1094eb34.ngrok.io/getUserChoices').subscribe(data => {
      console.log(JSON.parse(JSON.stringify(data)));
    });
  }
  
  cards = [ 
      new RecpCardComponent("Megan", 1000, "Tomatoes, onions, and garlic"),
      new RecpCardComponent("William", 2010, "Chocolate, celery, ketchup"),
      new RecpCardComponent("Kevin", 1000000, "Rotten cabbage, wasabi, rice"),
      new RecpCardComponent("Kevin", 1000100, "Rotten cabbage, wasabi, rice")
    ];
 
}
