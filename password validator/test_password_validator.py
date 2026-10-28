from password_validator import (
    has_min_length, has_uppercase, has_lowercase,
    has_digit, has_special, is_valid_password,
)
try:
    from password_validator import get_failed_requirements
except ImportError:
    get_failed_requirements = None

# special = any char that is not alphanumeric or whitespace
# get_failed_requirements order: min_length, uppercase, lowercase, digit, special

core_total = 0
core_fail  = 0
bonus_total = 0
bonus_fail  = 0

def check(label, got, expected, bonus=False):
    global core_total, core_fail, bonus_total, bonus_fail
    if bonus:
        bonus_total += 1
        if got != expected:
            bonus_fail += 1
            print(f"FAIL [{label}]")
            print(f"  expected: {expected!r}")
            print(f"  got:      {got!r}\n")
    else:
        core_total += 1
        if got != expected:
            core_fail += 1
            print(f"FAIL [{label}]")
            print(f"  expected: {expected!r}")
            print(f"  got:      {got!r}\n")

# ── has_min_length ───────────────────────────────────────────────────────────
check("has_min_length exactly 8",       has_min_length("Hello@12"),  True)
check("has_min_length more than 8",     has_min_length("Hello@123"), True)
check("has_min_length exactly 7",       has_min_length("1234567"),   False)  # boundary
check("has_min_length too short",       has_min_length("Hi@1"),      False)
check("has_min_length empty",           has_min_length(""),          False)

# ── has_uppercase ────────────────────────────────────────────────────────────
check("has_uppercase in mixed",         has_uppercase("Hello"),      True)
check("has_uppercase single char",      has_uppercase("A"),          True)
check("has_uppercase none",             has_uppercase("hello123!"),  False)
check("has_uppercase empty",            has_uppercase(""),           False)

# ── has_lowercase ────────────────────────────────────────────────────────────
check("has_lowercase in mixed",         has_lowercase("Hello"),      True)
check("has_lowercase single char",      has_lowercase("a"),          True)
check("has_lowercase none",             has_lowercase("HELLO123!"),  False)
check("has_lowercase empty",            has_lowercase(""),           False)

# ── has_digit ────────────────────────────────────────────────────────────────
check("has_digit present",              has_digit("abc1"),           True)
check("has_digit only",                 has_digit("1"),              True)
check("has_digit none",                 has_digit("abcdef!"),        False)
check("has_digit empty",                has_digit(""),               False)

# ── has_special ──────────────────────────────────────────────────────────────
check("has_special present",            has_special("abc!"),         True)
check("has_special only",               has_special("@"),            True)
check("has_special alnum only",         has_special("abc123"),       False)
check("has_special space not special",  has_special("Hello World"),  False)  # trap
check("has_special empty",              has_special(""),             False)

# ── is_valid_password ────────────────────────────────────────────────────────
check("valid: exactly 8 all pass",      is_valid_password("Hello@12"),  True)
check("valid: clearly valid",           is_valid_password("P@ssw0rd!"), True)
check("invalid: no uppercase",          is_valid_password("hello@12"),  False)
check("invalid: no lowercase",          is_valid_password("HELLO@12"),  False)
check("invalid: no digit",              is_valid_password("Hello@ab"),  False)
check("invalid: no special",            is_valid_password("Hello123"),  False)
check("invalid: too short",             is_valid_password("Hi@1"),      False)
check("invalid: empty",                 is_valid_password(""),          False)

print(f"\ncore: {core_total - core_fail}/{core_total} passed")
if core_fail == 0:
    print("BIM!!!")

# ── get_failed_requirements (bonus) ──────────────────────────────────────────
if get_failed_requirements is None or get_failed_requirements("Hello@12") is None:
    print("\nbonus: skipped (get_failed_requirements not implemented)")
else:
    check("no failures",              get_failed_requirements("Hello@12"),
          [],                                                                      bonus=True)
    check("missing uppercase",        get_failed_requirements("hello@12"),
          ["uppercase"],                                                            bonus=True)
    check("missing lowercase",        get_failed_requirements("HELLO@12"),
          ["lowercase"],                                                            bonus=True)
    check("missing digit",            get_failed_requirements("Hello@ab"),
          ["digit"],                                                                bonus=True)
    check("missing special",          get_failed_requirements("Hello123"),
          ["special"],                                                              bonus=True)
    check("too short only",           get_failed_requirements("Hi@1"),
          ["min_length"],                                                           bonus=True)
    check("all fail: empty string",   get_failed_requirements(""),
          ["min_length","uppercase","lowercase","digit","special"],                 bonus=True)
    check("space not special (trap)", get_failed_requirements("Hello 12"),
          ["special"],                                                              bonus=True)

    print(f"\nbonus: {bonus_total - bonus_fail}/{bonus_total} passed")