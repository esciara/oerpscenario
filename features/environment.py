# -*- coding: utf-8 -*-
# USE: BEHAVE_DEBUG_ON_ERROR=yes     (to enable debug-on-error)

from oerpscenario import environment


def before_all(ctx):
    environment.before_all(ctx)


def before_feature(ctx, feature):
    environment.before_feature(ctx, feature)


def before_scenario(ctx, scenario):
    environment.before_scenario(ctx, scenario)


def before_step(ctx, step):
    environment.before_step(ctx, step)


def after_step(ctx, laststep):
    environment.after_step(ctx, laststep)
