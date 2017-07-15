#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Blueprint

web_root = Blueprint("web_root", __name__, template_folder="templates")
