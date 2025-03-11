gamerScore = "1";
computerScore = 1;

sumScore = gamerScore + computerScore;

alert(sumScore);

function myGame() {
  player_name = prompt("enter your name");
  alert("hello " + player_name);
  player_geuss = prompt("geuss a number between 1 & 3");
  computer_geuss = randomInteger(1, 3);
  if (player_geuss == computer_geuss) {
    document.getElementById("user_feedback").innerHTML =
      "<i>Correct, you win</i>";
  } else {
    document.getElementById("user_feedback").innerHTML =
      "Incorrect, you lose\n" + "The computer geussed" + computer_geuss;
  }

  function randomInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
}
