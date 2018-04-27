import './.lib/pixi.js';

let app = null;

function init() {
  app = new PIXI.Application({
    width: document.body.clientWidth,
    height: document.body.clientHeight,
    backgroundColor: 0x330099
  });

  let circles = PIXI.Sprite.fromImage('images/circles.png');
  circles.anchor.set(0.5);
  circles.x = app.screen.width / 2;
  circles.y = app.screen.height / 2;
  app.stage.addChild(circles);
  app.ticker.add(function(delta) {
    circles.rotation += 0.01 * delta;
  });

  document.body.appendChild(app.view);
}

window.addEventListener('load', init);
