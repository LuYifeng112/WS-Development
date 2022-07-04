'''
This file hosts all the important plugins,

Apppearing - A Graphical Class for changing opacity based on distance of mouse
Random - A parser class for parsing statements from a list and choosing one randomly
Block - A parser class for packaging multiple statements
'''

init python:

    import math

    class Appearing(renpy.Displayable):

        def __init__(self, child, opaque_distance, transparent_distance, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(Appearing, self).__init__(**kwargs)

            # The child.
            self.child = renpy.displayable(child)

            # The distance at which the child will become fully opaque, and
            # where it will become fully transparent. The former must be less
            # than the latter.
            self.opaque_distance = opaque_distance
            self.transparent_distance = transparent_distance

            # The alpha channel of the child.
            self.alpha = 0.0

            # The width and height of us, and our child.
            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):

            # Create a transform, that can adjust the alpha channel of the
            # child.
            t = Transform(child=self.child, alpha=self.alpha)

            # Create a render from the child.
            child_render = renpy.render(t, width, height, st, at)

            # Get the size of the child.
            self.width, self.height = child_render.get_size()

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)

            # Blit (draw) the child's render to our render.
            render.blit(child_render, (0, 0))

            # Return the render.
            return render

        def event(self, ev, x, y, st):

            # Compute the distance between the center of this displayable and
            # the mouse pointer. The mouse pointer is supplied in x and y,
            # relative to the upper-left corner of the displayable.
            distance = math.hypot(x - (self.width / 2), y - (self.height / 2))

            # Base on the distance, figure out an alpha.
            if distance <= self.opaque_distance:
                alpha = 1.0
            elif distance >= self.transparent_distance:
                alpha = 0.0
            else:
                alpha = 1.0 - 1.0 * (distance - self.opaque_distance) / (self.transparent_distance - self.opaque_distance)

            # If the alpha has changed, trigger a redraw event.
            if alpha != self.alpha:
                self.alpha = alpha
                renpy.redraw(self, 0)

            # Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]


python early:

    def parse_random(l):

        # Looks for a colon at the end of the line.
        l.require(":")
        l.expect_eol()

        # This is a list of (weight, block) tuples.
        blocks = [ ]

        # ll is a lexer (an object that can match words, numbers, and other parts of text) that accesses the block under the current statement.
        ll = l.subblock_lexer()

        # For each line in the file, check for errors...
        while ll.advance():
            with ll.catch_error():

                # ...determine the weight...
                weight = 1.0

                if ll.keyword('weight'):
                    weight = float(ll.require(ll.float))

                # ...and then store the weight and the statement.
                blocks.append((weight, ll.renpy_statement()))

        return { "blocks" : blocks }

    def next_random(p):

        blocks = p["blocks"]

        # Pick a number between 0 and the total weight.
        total_weight = sum(i[0] for i in blocks)
        n = renpy.random.random() * total_weight

        # Then determine which block that number belongs to.
        for weight, block in blocks:
            if n <= weight:
                break
            else:
                n -= weight

        return block

    renpy.register_statement("random", parse=parse_random, next=next_random, predict_all=True, block=True)

python early:

    def parse_block(l):

        # Looks for a colon and the end of line.
        l.require(':')
        l.expect_eol()

        # Parses the block below this statement.
        block = l.subblock_lexer().renpy_block()

        return { "block" : block }

    # The next function returns the statement to execute next - in this case,
    # the first statement in the block.
    def next_block(p):
        return p["block"]

    renpy.register_statement("block", parse=parse_block, next=next_block, predict_all=True, block=True)