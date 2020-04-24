"""Generate a tikzpicture of a NN with two hidden layers."""
import datetime

from mako.template import Template

template = Template(filename='./templates/mlp_h2.template')
out = template.render(
    header=f'Generated by ninaa on {datetime.datetime.now().ctime()}.',
    png=True,
    inneurons=[f'in{i}' for i in range(2)],
    h1neurons=[f'h1{i}' for i in range(4)],
    h2neurons=[f'h2{i}' for i in range(3)],
    outneurons=[f'out{i}' for i in range(3)],
    neuron_color='viridisgreen',
    stroke=False)
with open('out.tex', 'w+') as f:
    f.write(out)
