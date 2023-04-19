from math import log, sqrt, pi, exp
from scipy.stats import norm

def d1(S,K,T,r,sigma):
    return(log(S/K)+(r+sigma**2/2.)*T) / (sigma*sqrt(T))
def d2(S,K,T,r,sigma):
    return d1(S,K,T,r,sigma)-sigma*sqrt(T)

def get_call_greeks(s, k, sigma, t, r, call_or_put) -> tuple:

    d1_ = d1(s, k, t, r, sigma)
    d2_ = d2(s, k, t, r, sigma)
    cdf_d1 = norm.cdf(d1_)
    pdf_d1 = norm.pdf(d1_)
    cdf_d2 = norm.cdf(d2_)
    pdf_d2 = norm.pdf(d2_)


    if call_or_put == "Call":
        delta = round(cdf_d1, 4)
        gamma = round(pdf_d1 / (s * sigma * sqrt(t)), 4)
        theta = round(0.01*(-(s* pdf_d1 *sigma)/(2*sqrt(t)) - r*k*exp(-r*t) * cdf_d2), 4)
        vega = round(0.01*(s* pdf_d1 *sqrt(t)), 4)
        rho = round(0.01*(k*t*exp(-r*t)*cdf_d2), 4)
        vanna = round(pdf_d1 * d2_ / sigma, 4)
        charm = round(-pdf_d1 * (2 * r * t - d2_ * sigma * sqrt(t)) / (2 * t * sigma * sqrt(t)), 4)
        vomma = round(0.01 * vega * d1_ * d2_ / sigma, 4)
        veta = round(-s * pdf_d1 * sqrt(t) * (r * d1_ / (sigma * sqrt(t)) - ((1 + d1_ * d2_) / (2 * t))), 4)
        speed = round(-gamma / s * (d1_ / (sigma * sqrt(t)) + 1), 4)
        zomma = round((gamma * d1_ * d2_ - 1) / sigma , 4)
        color = round(pdf_d1 / (2 * s * t * sigma * sqrt(t)) * (1 + d1_ * (2 * r * t - d2_ * sigma * sqrt(t)) / (sigma * sqrt)) , 4)
        #ultima = round( , 4)
        return (
            round(norm.cdf(d1_), 4),
            round(norm.pdf(d1_)/(s*sigma*sqrt(t)), 4),
            round(0.01*(-(s*norm.pdf(d1_)*sigma)/(2*sqrt(t)) - r*k*exp(-r*t)*norm.cdf(d2_)), 4),
            round(0.01*(s*norm.pdf(d1_)*sqrt(t)), 4),
            round(0.01*(k*t*exp(-r*t)*norm.cdf(d2_)), 4),
            round(norm.pdf(d1_) * d2_ / sigma, 4),
            round(-norm.pdf(d1_) * (2 * r * t - d2_ * sigma * sqrt(t)) / (2 * t * sigma * sqrt(t)), 4),
            round(0.01*(s*norm.pdf(d1_)*sqrt(t)) * d1_ * d2_ / sigma, 4),
            round(-s * norm.pdf(d1_) * sqrt(t) * (r * d1_ / (sigma * sqrt(t)) - ((1 + d1_ * d2_) / (2 * t))), 4),

        )
    else:
        return(
            round(-norm.cdf(-d1_), 4),
            round(norm.pdf(d1_)/(s*sigma*sqrt(t)), 4),
            round(0.01*(-(s*norm.pdf(d1_)*sigma)/(2*sqrt(t)) - r*k*exp(-r*t)*norm.cdf(d2_)), 4),
            round(0.01*(s*norm.pdf(d1_)*sqrt(t)), 4),
            round(0.01*(-k*t*exp(-r*t)*norm.cdf(-d2_)), 4),
            round(norm.pdf(d1_) * d2_ / sigma, 4),
            round(-norm.pdf(d1_) * (2 * r * t - d2_ * sigma * sqrt(t)) / 2 * t * sigma * sqrt(t), 4),
            round(0.01*(s*norm.pdf(d1_)*sqrt(t)) * d1_ * d2_ / sigma, 4),
            round(-s * norm.pdf(d1_) * sqrt(t) * (r * d1_ / (sigma * sqrt(t)) - ((1 + d1_ * d2_) / (2 * t))), 4)
        )

