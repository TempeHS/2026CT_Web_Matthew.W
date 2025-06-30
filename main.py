from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index ():
    card_data=(
        ("Basics", " Team Fortress 2 is a team-based shooter with nine unique classes, each serving different roles. To play effectively, learn the basics of each class, map layouts, and game objectives. Understanding teamwork, movement, and weapon choices is essential. With practice, you’ll quickly grasp the fun and strategy behind TF2’s gameplay. ", "Tips", "static/images/card_5.png"),
        ("Offensive class", " Scout, Soldier, and Pyro are the team’s frontline force. They rush in, disrupt enemy plans, and make space for others to shine. Scout brings speed, Soldier delivers explosive power, and Pyro thrives in close combat. Together, they’re the gritty trio that keeps the fight moving forward.🔥🚀💨 Ready to master them? ", "Tips", "static/images/card_1.png"),
        ("Defensive class", " Engineer, Heavy, and Demoman are vital to any strong TF2 defense. The Engineer builds and maintains defenses, the Heavy anchors the line with sustained firepower, and the Demoman controls space with traps and explosive area denial. Together, they form a resilient backbone that halts enemy advances and holds critical ground. 💣🔧💪🏼 ", "Tips", "static/images/card_2.png", "pricing.html"),
        ("Support class", " The support classes in TF2—Medic, Spy, and Sniper—play crucial behind-the-scenes roles. Medic keeps the team alive with healing and ÜberCharges, Spy disrupts the enemy from within with stealth and backstabs, and Sniper eliminates key threats. Together, they enable pushes, dismantle defenses, shaping the battlefield. 🩺🕵️‍♂️🎯 ", "Tips", "static/images/card_3.png"),
        ("Coaching", " Level up your TF2 skills with personalized coaching tailored to your goals. Sessions include expert VOD reviews, real-time feedback, mechanical drills, and class strategies. Track progress, master the metagame, and join a growth-focused community. Turn potential into performance—book your first session and start dominating with confidence and style. ", "Pay for coaching plan", "static/images/card_4.png"),
    )
    return render_template("index.html", cards = card_data), 200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/tips.html')
def tips():
    return render_template("tips.html"), 200

@app.route('/checkout.html')
def checkout():
    return render_template("checkout.html"), 200

@app.route('/pricing.html')
def pricing():
    return render_template("pricing.html"), 200

@app.route('/login.html')
def login():
    return render_template("login.html"), 200

if __name__ == '__main__':
    app.run(debug=True)
