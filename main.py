from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index ():
    card_data=(
        ("Offensive class", " Scout, Soldier, and Pyro are the team’s frontline force. They rush in, disrupt enemy plans, and make space for others to shine. Scout brings speed, Soldier delivers explosive power, and Pyro thrives in close combat. Together, they’re the gritty trio that keeps the fight moving forward.🔥🚀💨 Ready to master them? ", "Tips", "static/images/card_1.png"),
        ("Defensive class", " Engineer, Heavy, and Demoman are vital to any strong TF2 defense. The Engineer builds and maintains defenses, the Heavy anchors the line with sustained firepower, and the Demoman controls space with traps and explosive area denial. Together, they form a resilient backbone that halts enemy advances and holds critical ground. 💣🔧💪🏼 ", "Tips", "static/images/card_2.png"),
        ("Support class", " The support classes in TF2—Medic, Spy, and Sniper—play crucial behind-the-scenes roles. Medic keeps the team alive with healing and ÜberCharges, Spy disrupts the enemy from within with stealth and backstabs, and Sniper eliminates key threats. Together, they enable pushes, dismantle defenses, shaping the battlefield. 🩺🕵️‍♂️🎯 ", "Tips", "static/images/card_3.png"),
        ("Coaching", " Ready to level up your TF2 game? Our personalized coaching plan is your ticket to mastering every map, class, and clutch moment. Whether you're grinding to break into competitive play or just want to top the scoreboard in pubs, this plan adapts to your goals and playstyle. Each session includes expert VOD reviews, real-time feedback during matches, mechanical drills, and class-specific strategies to sharpen your edge. With progress tracking, tailored milestones, and scrim integration, you’ll see measurable improvement every step of the way. We don’t just teach gameplay—we build confidence, coordination, and a deeper understanding of TF2’s dynamic metagame. From rocket jumps to spy checks, you’ll walk away with tools that translate into real results. Join a community of players dedicated to growth, and let’s turn your potential into performance. Book your first session now and start dominating the battlefield—with style. ", "Pay for coaching plan", "static/images/coaching.png"),
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

if __name__ == '__main__':
    app.run(debug=True)
