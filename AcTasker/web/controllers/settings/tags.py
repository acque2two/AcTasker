#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import string

from flask import render_template, g, request, session, redirect

from AcTasker.db.schema import Tag
from AcTasker.web.libs.auth import need_login
from AcTasker.web.libs.error import Error
from AcTasker.web.web import web_root


@web_root.route("/settings/tags", methods=["GET"])
@need_login(no_redirect=False)
def web_setting_tags_get():
    tagmenu = [
        {
            "name":        "タグ名",
            "description": "タグにつけるタイトルを入力してください",
            "id":          "name",
            "type":        "text"
        },
        {
            "name":        "タグ詳細",
            "description": "タグに関する詳細情報を入力して下さい",
            "id":          "description",
            "type":        "text"
        },
        {
            "name":        "係数",
            "description": "優先度にかける係数を入力してください",
            "id":          "priority",
            "type":        "number",
        }
    ]

    return render_template("settings/tags.html",
                           **{"is_login": True
                               , "user":  g.user
                               , "menus": tagmenu
                               , "tags":  g.user.setting.tags
                              })


@web_root.route("/settings/tags", methods=["POST"])
@need_login(no_redirect=False)
def web_tags_add_post():
    if request.form.get('checked', None):
        if request.form.get("csrf_token", 'REQUEST_CSRF') == session.get("csrf_token", 'SESSION_CSRF'):
            g.user.setting.tags.append(
                Tag(
                    **{
                        "name":        request.form.get('name'),
                        "description": request.form.get('description'),
                        "priority":    request.form.get('priority')
                    }
                )
            )
            g.user.save()
            return redirect("/settings/tags")
        else:
            return Error.bad_request("CSRF_ERROR", "CSRF攻撃の可能性があります")

    if request.form.get('name', None) is None or request.form.get('description', None) is None or request.form.get(
            'priority', None):
        return redirect('/settings/tags')

    if len(g.user.setting.tags.filter(name=request.form.get('name', ''))) != 0:
        return redirect('/settings/tags')

    tagmenu = [
        {
            "name":        "タグ名",
            "description": "タグにつけるタイトルを入力してください",
            "id":          "name",
            "type":        "text",
            "value":       request.form.get("name")
        },
        {
            "name":        "タグ詳細",
            "description": "タグに関する詳細情報を入力して下さい",
            "id":          "description",
            "type":        "text",
            "value":       request.form.get("description")
        },
        {
            "name":        "係数",
            "description": "優先度にかける係数を入力してください",
            "id":          "priority",
            "type":        "number",
            "value":       request.form.get("priority")
        }
    ]

    session["csrf_token"] = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(64)])

    return render_template("settings/tags.html",
                           **{"is_login":          True,
                              "user":              g.user,
                              "menus":             tagmenu,
                              'checked':           True,
                              'csrf_token': session['csrf_token'],
                              "tags":              g.user.setting.tags
                              }
                           )


@web_root.route("/settings/tags/<string:tag_name>/modify", methods=["GET"])
@need_login(no_redirect=False)
def web_setting_tag_modify_get(tag_name):
    tag = g.user.setting.tags.filter(name=tag_name).first()
    if tag is None:
        return Error.not_found("タグが存在しません", "指定されたタグは存在しません。")

    tagmenu = [
        {
            "name":        "タグ名",
            "description": "タグにつけるタイトルを入力してください",
            "id":          "name",
            "type":        "text",
            'value':       tag.name
        },
        {
            "name":        "タグ詳細",
            "description": "タグに関する詳細情報を入力して下さい",
            "id":          "description",
            "type":        "text",
            'value':       tag.description
        },
        {
            "name":        "係数",
            "description": "優先度にかける係数を入力してください",
            "id":          "priority",
            "type":        "number",
            'value':       tag.priority
        }
    ]

    return render_template("settings/tags.html",
                           **{"is_login": True
                               , "user":  g.user
                               , "menus": tagmenu
                               , "tags":  g.user.setting.tags
                              })


@web_root.route("/settings/tags/<string:tag_name>/modify", methods=["POST"])
@need_login(no_redirect=False)
def web_setting_tag_modify_post(tag_name):
    tag = g.user.setting.tags.filter(name=tag_name).first()
    if tag is None:
        return Error.not_found("タグが存在しません", "指定されたタグは存在しません。")

    if request.form.get('checked', None):
        if request.form.get("csrf_token", 'REQUEST_CSRF') == session.get("csrf_token", 'SESSION_CSRF'):
            tag.name = request.form.get('name')
            tag.description = request.form.get('description')
            tag.priority = request.form.get('priority')
            tag.save()
            return redirect("/settings/tags")
        else:
            return Error.bad_request("CSRF_ERROR", "CSRF攻撃の可能性があります")

    tagmenu = [
        {
            "name":        "タグ名",
            "description": "タグにつけるタイトルを入力してください",
            "id":          "name",
            "type":        "text",
            "value":       request.form.get("name")
        },
        {
            "name":        "タグ詳細",
            "description": "タグに関する詳細情報を入力して下さい",
            "id":          "description",
            "type":        "text",
            "value":       request.form.get("description")
        },
        {
            "name":        "係数",
            "description": "優先度にかける係数を入力してください",
            "id":          "priority",
            "type":        "number",
            "value":       request.form.get("priority")
        }
    ]

    session["csrf_token"] = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(64)])

    return render_template("settings/tags.html",
                           **{"is_login":          True,
                              "user":              g.user,
                              "menus":             tagmenu,
                              'checked':           True,
                              'csrf_token': session['csrf_token'],
                              "tags":              g.user.setting.tags
                              }
                           )


@web_root.route("/settings/tags/<string:tag_name>/delete", methods=["GET"])
@need_login(no_redirect=False)
def web_setting_tag_delete_get(tag_name):
    tag = g.user.setting.tags.filter(name=tag_name).first()
    if tag is None:
        return Error.not_found("タグが存在しません", "指定されたタグは存在しません。")

    g.user.setting.tags.remove(tag)
    g.user.save()

    return redirect('/settings/tags')
