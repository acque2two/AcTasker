#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import string

from flask import render_template, g, session, request, redirect

from AcTasker.db.schema import Task
from AcTasker.web.libs.auth import need_login
from AcTasker.web.libs.error import Error
from AcTasker.web.web import web_root


@web_root.route("/tasks/add", methods=["GET"])
@need_login()
def web_tasks_add_get():
    if len(g.user.setting.tags) < 1:
        return Error.not_found("タグを先に追加してください。", "タグがないと登録できません。")

    taskmenu = [
        {
            "name":        "タスク名",
            "description": "タスクにつけるタイトルを入力してください",
            "id":          "name",
            "type":        "text"
        },
        {
            "name":        "タスク詳細",
            "description": "タスクに関する詳細情報を入力して下さい",
            "id":          "description",
            "type":        "text"
        },
        {
            "name":        "タグ",
            "description": "タスクにつけるタグを選択してください",
            "id":          "tag",
            "type":        "dropdown",
            "val":         [i.name for i in g.user.setting.tags]
        }
    ]
    return render_template("tasks/add.html",
                           **{"is_login": True, "menus": taskmenu})


@web_root.route("/tasks/add", methods=["POST"])
@need_login()
def web_tasks_add_post():
    if request.form.get('checked', None):
        if request.form.get("csrf_token", 'REQUEST_CSRF') == session.get("csrf_token", 'SESSION_CSRF'):
            g.user.tasks.append(
                Task(
                    **{
                        "name":        request.form.get('name'),
                        "description": request.form.get('description'),
                        "tag":         g.user.setting.tags.filter(name=request.form.get('tag')).first()
                    }
                )
            )
            g.user.tasks.save()
            g.user.save()
            return redirect("/tasks/add")
        else:
            return Error.bad_request("CSRF_ERROR", "CSRF攻撃の可能性があります")

    if request.form.get('name', None) is None or request.form.get('description', None) is None or request.form.get(
            'priority', None):
        return redirect('/tasks/add')

    if len(g.user.tasks.filter(name=request.form.get('name', ''))) != 0:
        return redirect('/tasks/add')

    taskmenu = [
        {
            "name":        "タスク名",
            "description": "タスクにつけるタイトルを入力してください",
            "id":          "name",
            "type":        "text",
            "value":       request.form.get("name")
        },
        {
            "name":        "タスク詳細",
            "description": "タスクに関する詳細情報を入力して下さい",
            "id":          "description",
            "type":        "text",
            "value":       request.form.get("description")
        },
        {
            "name":        "タグ",
            "description": "タスクにつけるタグを選択してください",
            "id":          "tag",
            "type":        "dropdown",
            "val":         [i.name for i in g.user.tasks],
            "value":       request.form.get("tag")
        }
    ]

    session["csrf_token"] = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(64)])

    return render_template("tasks/add.html",
                           **{"is_login":          True,
                              "user":              g.user,
                              "menus":             taskmenu,
                              'checked':           True,
                              'csrf_token': session['csrf_token'],
                              "tasks":             g.user.tasks
                              }
                           )
