from django.db import models


class Character(models.Model):
    """
    Model representing a DnD player character.
    """
    name = models.CharField(max_length=100, help_text="Enter a character name (fx. Legolas Greenleaf")
    level = models.IntegerField()
    frags = models.IntegerField(default=0)
    alive = models.BooleanField(default=True)

    CLASS_OPTIONS = (
        ('BB', 'Barbarian'),
        ('BA', 'Bard'),
        ('CL', 'Cleric'),
        ('DR', 'Druid'),
        ('FI', 'Fighter'),
        ('MO', 'Monk'),
        ('PA', 'Paladin'),
        ('RA', 'Ranger'),
        ('RO', 'Rogue'),
        ('SO', 'Sorcerer'),
        ('WA', 'Warlock'),
        ('WI', 'Wizard'),
    )

    player_super_class = models.CharField(max_length=2, choices=CLASS_OPTIONS,
                                          help_text="Select the main class of your character.")
    player_sub_class = models.CharField(max_length=50, help_text="Enter the subclass of your character")


    def __str__(self):
        """
        String for representing the Model object 
        """
        return "{}, level {} {} {}".format(self.name, self.level, self.player_sub_class, self.get_player_super_class_display())

