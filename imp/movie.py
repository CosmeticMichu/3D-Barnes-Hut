import imageio

filenames = []

for ii in range(0,100):
    name = 'figures/' + str(ii) + '.png'
    filenames.append(name)

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
#imageio.mimsave('figures/animation.gif', images)
imageio.mimsave('figures/animation.gif', images, duration = 60)