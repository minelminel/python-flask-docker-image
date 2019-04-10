from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify, Markup
import logging as logger
import json
from functools import wraps
import urllib3 as URL


class APIClass(object):
    """docstring for APIClass."""

    def __init__(self, Request=None,http=None):
        self.FullPath = Request
        self.EscapedStr = None if len(Request.split("api/?")) == 1 else Request.split("api/?")[-1]
        self.Message = "Hello, World! This is Michael"
