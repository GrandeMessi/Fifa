from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    short_name = db.Column(db.Text())
    overall = db.Column(db.Integer())
    age = db.Column(db.Integer())
    height_cm = db.Column(db.Integer())
    weight_kg = db.Column(db.Integer())
    club_name = db.Column(db.Text())
    club_position = db.Column(db.Text())
    nationality_name = db.Column(db.Text())
    skill_moves = db.Column(db.Integer())
    international_reputation = db.Column(db.Integer())
    pace = db.Column(db.Integer())
    shooting = db.Column(db.Integer())
    passing = db.Column(db.Integer())
    dribbling = db.Column(db.Integer())
    defending = db.Column(db.Integer())
    physic = db.Column(db.Integer())
    attacking_finishing = db.Column(db.Integer())
    attacking_heading_accuracy = db.Column(db.Integer())
    skill_dribbling = db.Column(db.Integer())

    def to_dict(self):
        return{
            'short_name': self.short_name,
            'overall': self.overall,
            'age': self.age,
            'height_cm': self.height_cm,
            'weight_kg': self.weight_kg,
            'club_name': self.club_name,
            'club_position': self.club_postion,
            'nationality_name': self.nationality_name,
            'skill_moves': self.skill_moves,
            'international_reputation': self.international_reputation,
            'pace': self.pace,
            'shooting': self.shooting,
            'passing': self.passing,
            'dribbling': self.dribbling,
            'defending': self.defending,
            'physic': self.physic,
            'attacking_finishing': self.attacking_finishing,
            'attacking_heading_accuracy': self.attacking_heading_accuracy,
            'skill_dribbling': self.skill_dribbling
        }
