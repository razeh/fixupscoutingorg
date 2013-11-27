# The BSA website is IE specific, for reasons I don't understand.  I've hacked
# up a bunch of changes here that fix most of the IE specific mistakes that they made.

def replace(s, index, replacement):
    l = list(s)
    l[index] = replacement
    return "".join(l)

def fix_all_usage(body):
    """ Replace every foo.all("x") call with foo.elements["x"] """
    while ".all(" in body:
        start = body.find(".all(")
        end = body.find(")", start)
        body = replace(body, end, "]")
        body = body.replace(".all(", ".elements[", 1)
    return body

def fix_drivers_license(body):
    """ Fix the drivers license number entry.   fix_all_usage must be applied first."""
    body = body.replace("""var ctllblDrvNum = frmCtl.elements["lblDrvNum"]""",
                        """var ctllblDrvNum = frmCtl.elements["txtDrvLicenseNum"];
       if (typeof ctllblDrvNum == "undefined") {
       ctllblDrvNum = frmCtl.elements["hdnlblDrvNum"];
       }
""")
    body = body.replace("""frmCtl.hdnlblDrvNum.value = ctllblDrvNum.innerText """,
                        """frmCtl.hdnlblDrvNum.value = ctllblDrvNum.value """)
    body = body.replace("""var ctllblDrvState = frmCtl.elements["lblDrvState"] ;""",
                        """var ctllblDrvState = frmCtl.elements["txtDrvLicenseState"] ;
       if (typeof ctllblDrvState == "undefined") {
            ctllblDrvState = frmCtl.elements["hdnlblDrvNum"];
       }
""")
    body = body.replace("""rmCtl.hdnlblDrvState.value = ctllblDrvState.innerText ;""",
                        """rmCtl.hdnlblDrvState.value = ctllblDrvState.value ;""")
    return body

# proxypy Entry methods
def proxy_mangle_request(req):
    return req

def proxy_mangle_response(res):
    if res is None:
        return res
    v = res.getHeader("Content-Type")
    if len(v) > 0:
        if ("application/x-javascript" in v[0]) or ("text/html" in v[0]):
            res.body = fix_all_usage(res.body)
            res.body = fix_drivers_license(res.body)
    return res


