# make bullet
if not player.is_hit:
    if shoot_frequency % 15 == 0:
        player.shoot(bullet_img)
    shoot_frequency += 1
    if shoot_frequency >= 15:
        shoot_frequency = 0

for bullet in player.bullets:
    #make speed of bullet not change
    bullet.move()
    # remove bullet if bullet out of screen
    if bullet.rect.bottom < 0:
        player.bullet.remove()

#display bullet
player.bullets.draw(screen)





















