from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='Test Activity', user='testuser', duration=10)
        self.assertEqual(activity.name, 'Test Activity')
        self.assertEqual(activity.duration, 10)

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Test Team', points=50)
        self.assertEqual(lb.team, 'Test Team')
        self.assertEqual(lb.points, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', difficulty='Medium')
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.difficulty, 'Medium')
